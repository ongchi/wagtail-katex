class Preview {
  constructor(previewId, bufferId, inputId) {
    this.preview = document.getElementById(previewId)
    this.buffer = document.getElementById(bufferId)
    this.input = document.getElementById(inputId)
    this.delay = 150 // delay after keystroke before updating
    this.timeout = null // store setTimout id

    this.input.addEventListener('input', () => {
      if (this.timeout) {
        clearTimeout(this.timeout)
      }
      this.timeout = setTimeout(() => {
        this.render()
      }, this.delay)
    })

    document.addEventListener('DOMContentLoaded', () => {
      this.render()
    })
  }

  render() {
    if (this.preview.innerHTML === this.input.value) {
      return
    }

    this.preview.innerHTML = this.input.value
    window.katex.render(this.input.value, this.preview, { throwOnError: false })
  }

  static renderToString(texString) {
    return window.katex.renderToString(texString)
  }

  static renderToElement(texString, el) {
    window.katex.render(texString, el)
  }
}
