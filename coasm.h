#pragma once

enum class opu_op_t {
  NO_OP = -1
  ,
ALU_OP = 0,
SFP_OP = 1,
TENSOR_OP = 2,
DP_OP = 3,
SP_OP = 4,
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
