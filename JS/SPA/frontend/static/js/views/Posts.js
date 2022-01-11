import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
  constructor() {
    super();
    this.setTitle("Posts")
  }

  async getHtml() {
    return `
      <h1> Welcome to Posts <h1>
      <p> This is Posts </p>
      <p>
        <a href="/" data-link> Get back to the dashboard </a>
      </p>
    `
  }
}