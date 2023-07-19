(() => {
  const React = window.React;
  const AtomicBlockUtils = window.DraftJS.AtomicBlockUtils;
  const EditorState = window.DraftJS.EditorState;
  const SelectionState = window.DraftJS.SelectionState;
  const Modifier = window.DraftJS.Modifier;
  const katex = window.katex;

  // Display a modal contains input textarea and preview
  function openKatexModal(katexInput, onConfirm) {
    // Input textarea
    const inputDiv = document.createElement("div");
    inputDiv.id = "wagtailkatex-modal-input";
    const inputArea = inputDiv.appendChild(document.createElement("textarea"));
    inputArea.spellcheck = false;
    inputArea.value = katexInput;

    // KaTeX rendered html output
    const katexOutputDiv = document.createElement("div");
    katexOutputDiv.id = "wagtailkatex-modal-output";

    // Action buttons
    const actionDiv = document.createElement("div");
    actionDiv.id = "wagtailkatex-modal-action";

    const cancelBtn = actionDiv.appendChild(document.createElement("button"));
    cancelBtn.type = "button";
    cancelBtn.className = "button no";
    cancelBtn.textContent = "Cancel";

    const confirmBtn = actionDiv.appendChild(document.createElement("button"));
    confirmBtn.type = "button";
    confirmBtn.className = "button";
    confirmBtn.textContent = "Confirm";

    // Modal setup
    const contentDiv = document.createElement("div");
    contentDiv.id = "wagtailkatex-modal-content";
    contentDiv.appendChild(inputDiv);
    contentDiv.appendChild(katexOutputDiv);
    contentDiv.appendChild(actionDiv);

    const modal = document.createElement("div");
    modal.id = "wagtailkatex-modal";
    modal.appendChild(contentDiv);

    const mainContent = document.querySelector("main#main");
    modal.style.width = `${mainContent.offsetWidth}px`;
    mainContent.appendChild(modal);

    katex.render(inputArea.value, katexOutputDiv, { throwOnError: false });

    // Event handling
    cancelBtn.onclick = () => closeKatexModal();
    confirmBtn.onclick = () => closeKatexModal(onConfirm);
    inputArea.addEventListener('input', (event) => {
      katex.render(event.target.value, katexOutputDiv, { throwOnError: false });
    });
    window.onclick = (event) => {
      if (event.target == modal) closeKatexModal();
    }

    const resizeObserver = new ResizeObserver((entries) => {
      entries.map((entry) => {
        modal.style.width = `${entry.target.offsetWidth}px`;
      })
    });
    resizeObserver.observe(mainContent);
  }

  function closeKatexModal(onConfirm) {
    let modal = document.getElementById("wagtailkatex-modal");

    if (onConfirm === undefined) {
      // Discard changes and close modal
      modal.remove();
    } else {
      // Verify and pass valid input to `onConfirm` to update editor state
      try {
        let texString = modal.querySelector("textarea").value;
        katex.renderToString(texString);
        onConfirm(texString);
        modal.remove();
      } catch (e) {
      }
    }
  }

  // Create new KaTeX entity in the editor, triggered by toolbar button
  class KaTeXSource extends React.Component {
    componentDidMount() {
      const editorState = this.props["editorState"];
      const entityType = this.props["entityType"];
      const onComplete = this.props["onComplete"];
      const content = editorState.getCurrentContent();

      openKatexModal("c = \\sqrt{a^2 + b^2}", (texString) => {
        const contentWithEntity = content.createEntity(
          entityType.type,
          "MUTABLE",
          { text: texString },
        );
        const entityKey = contentWithEntity.getLastCreatedEntityKey();

        const nextState = AtomicBlockUtils.insertAtomicBlock(
          editorState,
          entityKey,
          " ",
        );

        onComplete(nextState)
      });

      // Text editor will be blocked when canceled from the modal without this line
      onComplete(null);
    }

    render() {
      return null;
    }
  }

  // Render and editing an existing KaTeX entity
  class KaTeXBlock extends React.Component {
    // Open a modal for editing.
    openModal(onChange) {
      const block = this.props["block"];
      const blockProps = this.props["blockProps"];
      const editorState = blockProps["editorState"];
      const entity = blockProps["entity"];
      const katextEquation = entity.getData()["text"];

      openKatexModal(katextEquation, (texString) => {
        const nextState = this.updateBlockEntity(
          editorState,
          block,
          { text: texString }
        );
        onChange(nextState)
      })
    }

    updateBlockEntity(editorState, block, data) {
      const content = editorState.getCurrentContent();
      let nextContent = content.mergeEntityData(block.getEntityAt(0), data);
      nextContent = Modifier.mergeBlockData(
        nextContent,
        new SelectionState({
          anchorKey: block.getKey(),
          anchorOffset: 0,
          focusKey: block.getKey(),
          focusOffset: block.getLength(),
        }),
        {},
      );
      return EditorState.push(editorState, nextContent, "apply-entity");
    }

    render() {
      const blockProps = this.props["blockProps"];
      const entity = blockProps["entity"];
      const text = entity.getData()["text"];
      const onChange = blockProps["onChange"];

      return React.createElement("div", {
        role: "button",
        title: text,
        onMouseDown: () => this.openModal(onChange),
        dangerouslySetInnerHTML: {
          __html: katex.renderToString(text),
        },
      });
    }
  }

  window.draftail.registerPlugin({
    type: "KATEX-EMBED",
    source: KaTeXSource,
    block: KaTeXBlock,
  });
})();
