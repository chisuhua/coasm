#pragma once

#define COASM_BUILTIN_USE 1
// TODO below should be generate from coasm.py
// special sregs
#define SREG_M0 120  // default base register to share memory used by vop
#define SREG_TCC 106
#define SREG_TCCZ 107
#define SREG_VCC 121
#define SREG_VCCZ 122
#define SREG_EXEC 123
#define SREG_EXECZ 124
#define SREG_SCC 125
#define SREG_STACK_PTR 111
#define SREG_REGSPACE 110  // used to divide vreg space into share_memory/const

#define MAX_RESERVED_SREG_NUM 4

#define SREG_M0_STRIDE_BIT 0
#define SREG_M0_STRIDE_WIDTH 8

// special vregs
// VLS use kernal_param_base as vaddr, it will fetch adddress from param space
#define KERNEL_PARAM_BASE 62 // v[62:63]
#define LOCAL_MEM_PTR 60  // v[60:61]

// note is will decrease vreg since we reserve v63 down for const reg
#define KERNEL_CONST_REG_BASE_KERNEL_VIEW 59
// first 2 is reserve for kernel param and local mem ptr
//FIXME is is same as MAX_RESERVED_REG_NUM
// #define KERNEL_CONST_REG_BASE 4

// s[0:1] is reserved for local_stack_pointer
// #define BLOCK_CONST_REG_BASE_KERNEL_VIEW 2
#define BLOCK_CONST_REG_BASE 2
// v0/v1/v2 is used thread idx
#define THREAD_REG_BASE 0

// asm meta use kernel_ctrl to decode, the decode field is define
// for coasm_sregs (ptx_ir.h)
// the isasim will parse the ctrlbits and decide const buffer organize
#define KERNEL_CTRL_BIT_PARAM_BASE 0
#define KERNEL_CTRL_BIT_GRID_DIM_X 4
#define KERNEL_CTRL_BIT_GRID_DIM_Y 5
#define KERNEL_CTRL_BIT_GRID_DIM_Z 6
#define KERNEL_CTRL_BIT_BLOCK_DIM_X 7
#define KERNEL_CTRL_BIT_BLOCK_DIM_Y 8
#define KERNEL_CTRL_BIT_BLOCK_DIM_Z 9

#define KERNEL_CTRL_BIT_BLOCK_IDX_X 12
#define KERNEL_CTRL_BIT_BLOCK_IDX_Y 13
#define KERNEL_CTRL_BIT_BLOCK_IDX_Z 14

#define KERNEL_CTRL_BIT_THREAD_IDX_X 16
#define KERNEL_CTRL_BIT_THREAD_IDX_Y 17
#define KERNEL_CTRL_BIT_THREAD_IDX_Z 18

// # to generate from coasm.py ext_enc
#define COMMON_ENC_ext1_enc 0x7
#define COMMON_ENC_dsrc0_l 0x3
#define COMMON_ENC_dsrc0_d 0x2
#define COMMON_ENC_dsrc0_s 0x1
#define COMMON_ENC_dsrc0_v 0x0
#define COMMON_ENC_max_src0_32e_width 6
#define COMMON_ENC_max_src0_32e 63
#define COMMON_ENC_max_vsrc1_32e_width 6
#define COMMON_ENC_max_vsrc1_32e 63
#define COMMON_ENC_max_vdst_32e_width 6
#define COMMON_ENC_max_vdst_32e 63

#define COMMON_ENC_max_vdata_32e_width 6
#define COMMON_ENC_max_vdata_32e 63

#define COMMON_ENC_max_vaddr_32e_width 6
#define COMMON_ENC_max_vaddr_32e 63

#define COMMON_ENC_max_vls_offset_32e_width 7
#define COMMON_ENC_max_vls_offset_32e 127

#define COMMON_ENC_max_tcc_32e_width 2
#define COMMON_ENC_max_tcc_32e 3


#define COMMON_ENC_max_simm12_width 12
#define COMMON_ENC_max_simm12 ((1 < 12) -1)


// address space conversion
const unsigned long long _GLOBAL_HEAP_START = 0xC0000000;
// Volta max shmem size is 96kB
const unsigned long long _SHARED_MEM_SIZE_MAX = 96 * (1 << 10);
// Volta max local mem is 16kB
const unsigned long long _LOCAL_MEM_SIZE_MAX = 1 << 14;
// Volta Titan V has 80 SMs
const unsigned _MAX_STREAMING_MULTIPROCESSORS = 80;
// Max 2048 threads / SM
const unsigned _MAX_THREAD_PER_SM = 1 << 11;
// MAX 64 warps / SM
const unsigned _MAX_WARP_PER_SM = 1 << 6;

const unsigned long long _TOTAL_LOCAL_MEM_PER_SM = _MAX_THREAD_PER_SM * _LOCAL_MEM_SIZE_MAX;
const unsigned long long _TOTAL_SHARED_MEM = _MAX_STREAMING_MULTIPROCESSORS * _SHARED_MEM_SIZE_MAX;
const unsigned long long _TOTAL_LOCAL_MEM = _MAX_STREAMING_MULTIPROCESSORS * _MAX_THREAD_PER_SM * _LOCAL_MEM_SIZE_MAX;

const unsigned long long _SHARED_GENERIC_START = _GLOBAL_HEAP_START - _TOTAL_SHARED_MEM;
const unsigned long long _LOCAL_GENERIC_START = _SHARED_GENERIC_START - _TOTAL_LOCAL_MEM;
const unsigned long long _STATIC_ALLOC_LIMIT = _GLOBAL_HEAP_START - (_TOTAL_LOCAL_MEM + _TOTAL_SHARED_MEM);
