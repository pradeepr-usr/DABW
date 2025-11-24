"DABW"

activate dawb_env
cd DABW/
source dawb_env/bin/activate

cd DABW/Backend
run: uvicorn core.main:app --reload
