#pragma once

// special sregs
#define SREG_M0 120  // default base register to share memory used by vop
#define SREG_VCC 121
#define SREG_VCCZ 122
#define SREG_EXEC 123
#define SREG_EXECZ 124
#define SREG_SCC 125
#define SREG_STACK_PTR 111
#define SREG_REGSPACE 110  // used to divide vreg space into share_memory/const

// special vregs
// VLS use kernal_param_base as vaddr, it will fetch adddress from param space
#define KERNEL_PARAM_BASE 62 // v[62:63]
#define LOCAL_MEM_PTR 60  // v[60:61]

// note is will decrease vreg since we reserve v63 down for const reg
#define KERNEL_CONST_REG_BASE_KERNEL_VIEW 59
// first 2 is reserve for kernel param and local mem ptr
#define KERNEL_CONST_REG_BASE 4

// s[0:1] is reserved for local_stack_pointer
// #define BLOCK_CONST_REG_BASE_KERNEL_VIEW 2
#define BLOCK_CONST_REG_BASE 2
// v0/v1/v2 is used thread idx
#define THREAD_REG_BASE 0

// asm meta use kernel_ctrl to decode, the decode field is define
// for coasm_sregs (ptx_ir.h)
// the isasim will parse the ctrlbits and decide const buffer organize
#define KERNEL_CTRL_BIT_GRID_DIM_X 0
#define KERNEL_CTRL_BIT_GRID_DIM_Y 1
#define KERNEL_CTRL_BIT_GRID_DIM_Z 2
#define KERNEL_CTRL_BIT_BLOCK_DIM_X 3
#define KERNEL_CTRL_BIT_BLOCK_DIM_Y 4
#define KERNEL_CTRL_BIT_BLOCK_DIM_Z 5

#define KERNEL_CTRL_BIT_BLOCK_IDX_X 6
#define KERNEL_CTRL_BIT_BLOCK_IDX_Y 7
#define KERNEL_CTRL_BIT_BLOCK_IDX_Z 8

#define KERNEL_CTRL_BIT_THREAD_IDX_X 16
#define KERNEL_CTRL_BIT_THREAD_IDX_Y 17
#define KERNEL_CTRL_BIT_THREAD_IDX_Z 18
