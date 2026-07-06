{
  description = "Neuromatch Academy Computational Neuroscience — dev shell";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true; # torch, cuda-adjacent bits
      };

      python = pkgs.python312;

      pyEnv = python.withPackages (ps: with ps; [
        # --- NMA requirements.txt / environment.yml ---
        requests
        numpy
        scipy
        matplotlib
        scikit-learn
        torch            # CPU build; swap to torchWithCuda if a GPU box
        torchvision
        ipywidgets
        tqdm
        pandas
        decorator
        h5py
        opencv4          # provides cv2
        natsort
        # --- later-week libraries (W2D2 signal proc, W3D5 causality) ---
        mne              # W2D2: time-frequency (tfr_array_morlet), EEG/MEG signal tools
        statsmodels      # W3D5: grangercausalitytests (network causality)
        # --- notebook stack ---
        jupyterlab
        notebook
        ipykernel
        # --- handy extras NMA notebooks pull in ---
        seaborn
        pillow
        nest-asyncio
      ]);
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = [ pyEnv pkgs.git ];

        shellHook = ''
          echo "NMA CompNeuro devshell — python $(python --version 2>&1 | cut -d' ' -f2)"
          # Register this env as a Jupyter kernel so `jupyter lab` sees it.
          python -m ipykernel install --user --name nma-compneuro \
            --display-name "Python (NMA)" >/dev/null 2>&1 || true
          echo "run:  jupyter lab   (kernel: Python (NMA))"
        '';
      };
    };
}
