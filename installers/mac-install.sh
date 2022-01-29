cd $HOME
conda update -y -n base conda
conda config --add channels conda-forge
conda config --set channel_priority strict
conda create -y -n qis101 python=3.9
conda activate qis101
conda install -y matplotlib sympy scipy scikit-learn
conda install -y pandas pandasql docutils pandocfilters
conda install -y numexpr h5py traitsui zipp pathspec openpyxl
conda install -y pylint autopep8 black
conda install -y websockets requests pyserial
conda install -y ipython ipykernel ipympl
conda install -y jupyterlab jupyterlab_code_formatter
conda install -y numba
pip install pygame
pip install 'qiskit[all]'
pip install 'qiskit[visualization]'
conda update -y --all
echo 'y' | jupyter lab --generate-config
echo 'c.ServerApp.use_redirect_file = False' >> $HOME/.jupyter/jupyter_lab_config.py
