#!/bin/bash
# day-3 training batches, back to back (3 members each, 1 thread per member):
#  A (already running): 12 epochs, seeds 17-19          -> work/gru_e12_s*.npz
#  B: 8 epochs, final-layer loss weight 8, seeds 20-22  -> work/gru_fw8_s*.npz
#  C: 8 epochs, hidden 48, seeds 23-25                   -> work/gru_h48_s*.npz
#  D: 8 epochs, all data (full + mini, no holdout), 26-28 -> work/gru_all8_s*.npz
cd /home/user/arc-whitebox
source work/lean_env.sh
done3() { [ "$(grep -l 'saved work/' $1 $2 $3 2>/dev/null | wc -l)" -ge 3 ]; }
until done3 work/runs/gru_e12_s17.log work/runs/gru_e12_s18.log work/runs/gru_e12_s19.log; do sleep 60; done
echo "$(date -u +%H:%M) A done"
for sd in 20 21 22; do OMP_NUM_THREADS=1 setsid nohup python work/gru_corr.py --full --hold-mini --hidden 64 --epochs 8 --inner 2 --seed $sd --act cdf --lr 5e-4 --wd 1e-5 --final-w 8 --out work/gru_fw8_s$sd.npz > work/runs/gru_fw8_s$sd.log 2>&1 & done
until done3 work/runs/gru_fw8_s20.log work/runs/gru_fw8_s21.log work/runs/gru_fw8_s22.log; do sleep 60; done
echo "$(date -u +%H:%M) B done"
for sd in 23 24 25; do OMP_NUM_THREADS=1 setsid nohup python work/gru_corr.py --full --hold-mini --hidden 48 --epochs 8 --inner 2 --seed $sd --act cdf --lr 5e-4 --wd 1e-5 --out work/gru_h48_s$sd.npz > work/runs/gru_h48_s$sd.log 2>&1 & done
until done3 work/runs/gru_h48_s23.log work/runs/gru_h48_s24.log work/runs/gru_h48_s25.log; do sleep 60; done
echo "$(date -u +%H:%M) C done"
for sd in 26 27 28; do OMP_NUM_THREADS=1 setsid nohup python work/gru_corr.py --full --holdout 0 --hidden 64 --epochs 8 --inner 2 --seed $sd --act cdf --lr 5e-4 --wd 1e-5 --out work/gru_all8_s$sd.npz > work/runs/gru_all8_s$sd.log 2>&1 & done
until done3 work/runs/gru_all8_s26.log work/runs/gru_all8_s27.log work/runs/gru_all8_s28.log; do sleep 60; done
echo "$(date -u +%H:%M) D done"
