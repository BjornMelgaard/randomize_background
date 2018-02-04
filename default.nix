{
  pkgs ? import <nixpkgs> {}
}:

with pkgs;

let
  python = python3;
  pythonPackages = python.pkgs;
in

pythonPackages.buildPythonApplication rec {
  pname = "randomize_background";
  version = "0.0.1";
  name = "${pname}-${version}";

  src = ./.;

  buildInputs = [
    python
    feh
  ];

  meta = {
    homepage = https://github.com/BjornMelgaard/randomize_background;
    description = "randomize_background ~/wallpallers/*";
    license = lib.licenses.mit;
    platforms = lib.platforms.all;
  };
}
