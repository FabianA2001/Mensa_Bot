{
  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
    pyproject-nix = {
      url = "github:nix-community/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, pyproject-nix }: let
    inherit (nixpkgs.legacyPackages.x86_64-linux) python3;
    project = pyproject-nix.lib.project.loadPyproject { projectRoot = ./.; };
  in {
    packages.x86_64-linux = rec {
      mensaapi = python3.pkgs.buildPythonPackage (project.renderers.buildPythonPackage { python = python3; });
      default = mensaapi;
    };
  };
}
