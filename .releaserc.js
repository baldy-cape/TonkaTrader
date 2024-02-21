// This configuration is for semantic-release and is used to automate the release process
// within GitHub Actions. It specifies the plugins to analyze commits, generate release notes,
// and manage GitHub releases, excluding npm publishing steps.

module.exports = {
  branches: ["main"],
  plugins: [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/github"
  ]
};
