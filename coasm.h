#pragma once

enum class opu_op_t {
  NO_OP = -1
  ,
INT_OP = 0,
INT_LONG_OP = 1,
SP_OP = 2,
DP_OP = 18,
SFU_OP = 3,
TENSOR_OP = 4,
INTP_OP = 5,
ALU_SFU_OP = 6,
TENSOR_LOAD_OP = 7,
TENSOR_STORE_OP = 8,
LOAD_OP = 9,
STORE_OP = 10,
BRANCH_OP = 11,
BARRIER_OP = 12,
MEMORY_BARRIER_OP = 13,
WAITCNT_OP = 14,
CALL_OP = 15,
RET_OP = 16,
EXIT_OP = 17
};

enum class opu_atomic_t {
  INVALID = -1
  ,
ATOMIC_POPC = 0,
ATOMIC_AND = 1,
ATOMIC_OR = 2,
ATOMIC_XOR = 3,
ATOMIC_CAS = 4,
ATOMIC_EXCH = 5,
ATOMIC_ADD = 6,
ATOMIC_INC = 7,
ATOMIC_DEC = 8,
ATOMIC_MIN = 9,
ATOMIC_MAX = 10
};

enum class opu_datatype_t {
  INVALID = -1
  ,
DT_INT8 = 0,
DT_UINT8 = 1,
DT_INT16 = 2,
DT_UINT16 = 3,
DT_INT32 = 4,
DT_UINT32 = 5,
DT_FP16 = 6,
DT_BF16 = 7,
DT_TF32 = 8,
DT_FP32 = 9,
DT_B16 = 10,
DT_B32 = 11,
DT_I16x2 = 12,
DT_U16x2 = 13,
DT_B16x2 = 14,
DT_FP16x2 = 15,
DT_BF16x2 = 16,
DT_INT64 = 17,
DT_UINT64 = 18,
DT_B64 = 19,
DT_MAX = 99
};

enum class opu_cacheop_t {
  INVALID = -1
  ,
CACHE_ALL = 0,
CACHE_LAST_USE = 1,
CACHE_VOLATILE = 2,
CACHE_L1 = 3,
CACHE_STREAMING = 4,
CACHE_GLOBAL = 5,
CACHE_WRITE_BACK = 6,
CACHE_WRITE_THROUGH = 7
};

enum class opu_mspace_t {
  
INVALID = 0,
GLOBAL = 1,
SHARED = 2,
PRIVATE = 3,
CONST = 4,
PARAM = 5
};

enum class opu_memop_t {
  
INVALID = 0,
LOAD = 1,
STORE = 2
};

enum class opu_pipeline_t {
  
SP__OP = 0,
DP__OP = 1,
INT__OP = 2,
SFU__OP = 3,
TENSOR__OP = 4,
MEM__OP = 5,
SPECIALIZED__OP = 6
};
