RESULTS = [({'binary': '../out-perf/benchmarks/dbtest', 'log_fake_writes': False, 'retry': False, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks', 'db': 'kvdb-st', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 1, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': False, 'log_compress': False}, [(38179.9, 38179.9, 0.0261386, 0.0, 0.0), (38455.4, 38455.4, 0.0259527, 0.0, 0.0), (38349.3, 38349.3, 0.0260178, 0.0, 0.0)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 1, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(27279.2, 27279.2, 0.0365973, 0.0, 0.0), (27155.6, 27155.6, 0.0367648, 0.0, 0.0), (26796.8, 26796.8, 0.037253, 0.0, 0.0)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 1, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(26321.0, 26321.0, 0.0379286, 0.0, 0.0), (26569.2, 26569.2, 0.037573, 0.0, 0.0), (27140.4, 27140.4, 0.0367824, 0.0, 0.0)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 1, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(26820.0, 26820.0, 0.0372239, 0.0, 0.0), (26198.6, 26198.6, 0.0381046, 0.0, 0.0), (26721.0, 26721.0, 0.0373651, 0.0, 0.0)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-fast-id-gen', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 1, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(27636.2, 27636.2, 0.0361241, 0.0, 0.0), (27896.6, 27896.6, 0.0357849, 0.0, 0.0), (27195.4, 27195.4, 0.0367132, 0.0, 0.0)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 2, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(53665.2, 53665.2, 0.0371825, 0.0, 2.33332), (55335.5, 55335.5, 0.0360387, 0.0, 2.99998), (55456.1, 55456.1, 0.0359656, 0.0, 2.44999)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 2, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(54570.7, 54570.7, 0.0365389, 0.0, 2.76665), (55027.4, 55027.4, 0.0362424, 0.0, 2.64998), (52970.9, 52970.9, 0.0376617, 0.0, 2.29999)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 2, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(54740.4, 54740.4, 0.0364358, 0.0, 2.51665), (53974.4, 53974.4, 0.0369523, 0.0, 2.79998), (53956.9, 53956.9, 0.0369649, 0.0, 2.66665)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-fast-id-gen', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 2, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(55583.4, 55583.4, 0.0358752, 0.0, 2.74998), (55511.9, 55511.9, 0.0359357, 0.0, 2.81665), (55076.5, 55076.5, 0.0362123, 0.0, 2.83332)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 4, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(102115.0, 102115.0, 0.0389772, 0.0, 14.9832), (102483.0, 102483.0, 0.0388438, 0.0, 15.1499), (99394.2, 99394.2, 0.0400376, 0.0, 15.4666)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 4, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(99742.6, 99742.6, 0.0399078, 0.0, 14.7833), (99686.9, 99686.9, 0.0399313, 0.0, 15.0999), (98806.6, 98806.6, 0.0402783, 0.0, 15.0666)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 4, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(101562.0, 101562.0, 0.0391926, 0.0, 14.7999), (101148.0, 101148.0, 0.03935, 0.0, 14.8499), (100588.0, 100588.0, 0.0395722, 0.0, 14.3666)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-fast-id-gen', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 4, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(101855.0, 101855.0, 0.0390631, 0.0, 16.1166), (103506.0, 103506.0, 0.0384577, 0.0, 15.6666), (104612.0, 104612.0, 0.0380519, 0.0, 14.6166)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 6, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(105894.0, 105894.0, 0.0402846, 0.0, 1781.74), (106271.0, 106271.0, 0.0401367, 0.0, 1796.52), (103814.0, 103814.0, 0.0411498, 0.0, 1772.05)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 6, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(103324.0, 103324.0, 0.0413357, 0.0, 1784.36), (107888.0, 107888.0, 0.0394036, 0.0, 1793.97), (105044.0, 105044.0, 0.0406493, 0.0, 1787.03)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 6, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(104675.0, 104675.0, 0.0407454, 0.0, 1819.53), (103649.0, 103649.0, 0.0411788, 0.0, 1792.34), (105401.0, 105401.0, 0.0404608, 0.0, 1828.0)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-fast-id-gen', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 6, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(118134.0, 118134.0, 0.0462966, 0.0, 459.179), (116671.0, 116671.0, 0.0467614, 0.0, 451.031), (120292.0, 120292.0, 0.0458435, 0.0, 503.747)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 8, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(110164.0, 110164.0, 0.0415078, 0.0, 3593.76), (109447.0, 109447.0, 0.0417149, 0.0, 3590.73), (109431.0, 109431.0, 0.0418349, 0.0, 3584.31)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 8, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(107558.0, 107558.0, 0.0427503, 0.0, 3538.26), (108211.0, 108211.0, 0.042309, 0.0, 3571.77), (108623.0, 108623.0, 0.0421955, 0.0, 3573.84)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 8, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(103702.0, 103702.0, 0.0444855, 0.0, 3527.93), (107269.0, 107269.0, 0.0427647, 0.0, 3571.43), (110737.0, 110737.0, 0.041177, 0.0, 3588.79)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-fast-id-gen', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 8, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(142348.0, 142348.0, 0.0479053, 0.0, 939.884), (137373.0, 137373.0, 0.0501871, 0.0, 917.892), (138177.0, 138177.0, 0.0498929, 0.0, 916.069)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 10, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(109780.0, 109780.0, 0.0442741, 0.0, 5086.42), (107663.0, 107663.0, 0.0452148, 0.0, 5028.67), (108948.0, 108948.0, 0.0446894, 0.0, 5072.1)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 10, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(109759.0, 109759.0, 0.0442411, 0.0, 5083.12), (108137.0, 108137.0, 0.0450479, 0.0, 5057.78), (108815.0, 108815.0, 0.04471, 0.0, 5038.11)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 10, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(106691.0, 106691.0, 0.0458682, 0.0, 5043.55), (108021.0, 108021.0, 0.0450373, 0.0, 5041.45), (110638.0, 110638.0, 0.0437823, 0.0, 5068.65)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-fast-id-gen', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 10, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(129149.0, 129149.0, 0.0540999, 0.0, 1050.48), (109476.0, 109476.0, 0.0503589, 0.0, 924.406), (142261.0, 142261.0, 0.0537856, 0.0, 1222.93)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 12, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(112102.0, 112102.0, 0.045725, 0.0, 6523.81), (112269.0, 112269.0, 0.0455701, 0.0, 6531.66), (111602.0, 111602.0, 0.0459453, 0.0, 6530.73)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 12, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(109293.0, 109293.0, 0.0469943, 0.0, 6478.34), (111680.0, 111680.0, 0.0460389, 0.0, 6533.16), (110390.0, 110390.0, 0.0465508, 0.0, 6495.78)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 12, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(107479.0, 107479.0, 0.0480774, 0.0, 6462.35), (111586.0, 111586.0, 0.0459079, 0.0, 6531.83), (110096.0, 110096.0, 0.0466755, 0.0, 6489.14)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-fast-id-gen', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 12, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(151740.0, 151740.0, 0.056124, 0.0, 1667.71), (102389.0, 102389.0, 0.0534389, 0.0, 1073.26), (147175.0, 147175.0, 0.0557127, 0.0, 1616.25)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 16, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(112078.0, 112078.0, 0.0503686, 0.0, 9258.67), (110439.0, 110439.0, 0.0512938, 0.0, 9228.7), (112589.0, 112589.0, 0.0498881, 0.0, 9275.0)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 16, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(110793.0, 110793.0, 0.0509917, 0.0, 9266.3), (111479.0, 111479.0, 0.050596, 0.0, 9230.4), (113947.0, 113947.0, 0.0492867, 0.0, 9307.76)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 16, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(114086.0, 114086.0, 0.0490479, 0.0, 9354.82), (112389.0, 112389.0, 0.0500887, 0.0, 9263.79), (112203.0, 112203.0, 0.0501601, 0.0, 9268.97)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-fast-id-gen', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 16, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(96140.3, 96140.3, 0.0602456, 0.0, 1317.04), (123833.0, 123833.0, 0.0586249, 0.0, 1612.86), (91066.7, 91066.7, 0.0622132, 0.0, 1227.0)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 20, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(113260.0, 113260.0, 0.053017, 0.0, 11754.7), (112459.0, 112459.0, 0.053476, 0.0, 11714.3), (112940.0, 112940.0, 0.0533785, 0.0, 11758.2)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 20, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(112123.0, 112123.0, 0.0534119, 0.0, 11666.5), (115343.0, 115343.0, 0.0518274, 0.0, 11819.3), (110106.0, 110106.0, 0.0551375, 0.0, 11655.7)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 20, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(111807.0, 111807.0, 0.0539485, 0.0, 11719.9), (112420.0, 112420.0, 0.0538304, 0.0, 11787.5), (113152.0, 113152.0, 0.052745, 0.0, 11688.3)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-fast-id-gen', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 20, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(129850.0, 129850.0, 0.0655325, 0.0, 1906.86), (113485.0, 113485.0, 0.0637675, 0.0, 1613.24), (129069.0, 129069.0, 0.0640064, 0.0, 1774.91)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 24, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(112045.0, 112045.0, 0.0562702, 0.0, 13864.4), (112644.0, 112644.0, 0.0561196, 0.0, 13896.3), (109792.0, 109792.0, 0.0558557, 0.0, 13456.0)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 24, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(112941.0, 112941.0, 0.0558932, 0.0, 13915.8), (113446.0, 113446.0, 0.0542462, 0.0, 13645.3), (112769.0, 112769.0, 0.0559335, 0.0, 13895.2)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 24, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(112793.0, 112793.0, 0.0559056, 0.0, 13849.6), (112508.0, 112508.0, 0.0558038, 0.0, 13815.1), (111499.0, 111499.0, 0.0569646, 0.0, 13887.4)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-fast-id-gen', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 24, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(120387.0, 120387.0, 0.064223, 0.0, 1863.88), (92974.0, 92974.0, 0.0662328, 0.0, 1458.06), (142175.0, 142175.0, 0.0656398, 0.0, 2178.4)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 28, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(111017.0, 111017.0, 0.0584187, 0.0, 15620.5), (115832.0, 115832.0, 0.056032, 0.0, 16005.3), (109617.0, 109617.0, 0.0594124, 0.0, 15484.4)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 28, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(96515.9, 96515.9, 0.0568733, 0.0, 13313.0), (111291.0, 111291.0, 0.057934, 0.0, 15575.5), (112729.0, 112729.0, 0.0574871, 0.0, 15752.4)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 28, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(111314.0, 111314.0, 0.0587607, 0.0, 15708.9), (102549.0, 102549.0, 0.0573524, 0.0, 14308.9), (112734.0, 112734.0, 0.0576216, 0.0, 15792.8)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-fast-id-gen', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 28, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(125184.0, 125184.0, 0.0663509, 0.0, 1955.04), (94220.5, 94220.5, 0.0677441, 0.0, 1598.4), (105873.0, 105873.0, 0.0695081, 0.0, 1697.33)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 32, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(93351.6, 93351.6, 0.060823, 0.0, 13923.2), (107609.0, 107609.0, 0.0615199, 0.0, 16512.1), (102195.0, 102195.0, 0.0653834, 0.0, 15340.9)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 32, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(103391.0, 103391.0, 0.0650066, 0.0, 15606.9), (90638.3, 90638.3, 0.0607784, 0.0, 13671.9), (106724.0, 106724.0, 0.0613764, 0.0, 16335.3)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 32, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(106892.0, 106892.0, 0.0621241, 0.0, 16275.5), (102397.0, 102397.0, 0.0621106, 0.0, 15317.1), (107323.0, 107323.0, 0.0606884, 0.0, 16274.8)]), ({'binary': '../out-backoff/benchmarks/dbtest', 'log_fake_writes': False, 'retry': True, 'scale_factor': 4, 'name': 'multipart:skew', 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-fast-id-gen', 'db': 'ndb-proto2', 'bench': 'tpcc', 'par_load': False, 'disable_gc': False, 'threads': 32, 'numa_memory': None, 'persist': 'persist-none', 'disable_snapshots': False, 'log_nofsync': False, 'backoff': True, 'log_compress': False}, [(95339.6, 95339.6, 0.0722419, 0.0, 1606.52), (132200.0, 132200.0, 0.074819, 0.0, 2214.72), (89102.4, 89102.4, 0.0709545, 0.0, 1390.29)])]
