# For more in https://search.nixos.org/packages
{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = with pkgs; [
    git
    gitleaks
    gh
    pre-commit
    go-task
    yamllint
  ];
}
