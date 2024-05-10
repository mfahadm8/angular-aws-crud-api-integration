
mkfile_path:= $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir:= $(dir $(mkfile_path))


build-UserCrudLambda: 
ifeq ($(OS), Windows_NT)
	copy "$(mkfile_dir)src/UserCrudLambda" "$(ARTIFACTS_DIR)"
else
	cp "$(mkfile_dir)src/UserCrudLambda" "$(ARTIFACTS_DIR)"
endif
	python -m pip install -r "$(mkfile_dir)src/UserCrudLambda/requirements.txt" -t "$(ARTIFACTS_DIR)/"
