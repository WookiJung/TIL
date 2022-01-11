import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
  constructor() {
    super();
    this.setTitle("Settings")
  }

  async getHtml() {
    return `
      <h1> Welcome to Settings <h1>
      <p> Manage your privacy</p>
      <p>
        <a href="/" data-link>Get back to the dashboard</a>
      </p>
    `
  }
}