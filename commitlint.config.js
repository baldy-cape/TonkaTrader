// commitlint.config.js

// This configuration file is for commitlint, a tool used to enforce commit message standards.
// It helps maintain a consistent commit history and automate versioning and changelog generation.
// The configuration extends '@commitlint/config-conventional' which is a set of rules based on
// the Conventional Commits specification. This specification outlines a standard format for
// commit messages, making them more readable and enabling automatic determination of semantic
// version bumps.

module.exports = {
  // Extend the conventional commit configuration. This includes rules for types such as
  // feat, fix, chore, docs, etc., and enforces the structure of the commit message.
  extends: ['@commitlint/config-conventional'],
};

