<!-- BEGIN_DOCS -->
<div align="center">

<a name="readme-top"></a>

<img alt="gif-header" src="https://github.com/lpsm-dev/lpsm-dev/blob/main/.github/assets/gif-header.gif" width="225"/>

<h2>Tech Challenges</h2>

[![Semantic Release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)]()
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)]()

---

<img alt="gif-about" src="https://github.com/lpsm-dev/lpsm-dev/blob/main/.github/assets/gif-about.gif" width="225"/>

<p>The idea is to bring together things I've learned along my IT journey</p>

<p>
  <a href="#-getting-started-">Getting Started</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-concepts-">Concepts</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-versioning-">Versioning</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-troubleshooting-">Troubleshooting</a>
</p>

</div>

---

## ➤ Getting Started

### Setup

To configure your system for the development of this project, follow the steps below:

- Clone the git repository to your local environment.
- Install [asdf](https://asdf-vm.com/) to manage runtime dependencies.
- Install runtime dependencies.

```bash
cut -d' ' -f1 .tool-versions | xargs -I{} sh -c 'asdf plugin add "$1"' -- {} && asdf install
```

- Follow the instructions after installing the tools in `.tool-versions` with `asdf`.
- Run task from the root of the repository to see available commands. We use task in place of make for this project. See [Taskfile.yml](Taskfile.yml) for more information.

### Direnv

Set the sensitive information in a .env file and run this command:

```bash
export $(grep -v '^#' .env | xargs)
```

### Nix Shell

In this project, we are implementing Nix Shell to facilitate setting up a new environment with all the tools we are likely to use.

To do this, we configure the 'shell.nix' file, where we specify the tools we need one by one.

To generate this temporary environment, run the following command:

```bash
nix-shell
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## ➤ Versioning

To check the change history, please access the [**CHANGELOG.md**](CHANGELOG.md) file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## ➤ Troubleshooting

If you have any problems, [open an issue in this project](https://github.com/lpsm-dev/docker-crypto-miner/issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## ➤ Show your support

<div align="center">

Give me a ⭐️ if this project helped you!

<img alt="gif-footer" src="https://github.com/lpsm-dev/lpsm-dev/blob/main/.github/assets/yoda.gif" width="225"/>

Made with 💜 by [me](https://github.com/lpsm-dev) 👋 inspired on [readme-md-generator](https://github.com/kefranabg/readme-md-generator)
