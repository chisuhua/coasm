	.text
	.amdgcn_target "amdgcn-amd-amdhsa--gfx803"
	.globl	fadd                            ; -- Begin function fadd
	.p2align	8
	.type	fadd,@function
fadd:                                   ; @fadd
; %bb.0:                                ; %entry
	s_load_dwordx4 s[0:3], s[4:5], 0x0
	s_load_dwordx4 s[4:7], s[4:5], 0x10
	s_waitcnt lgkmcnt(0)
	v_mov_b32_e32 v0, s0
	v_mov_b32_e32 v1, s1
	s_load_dword s0, s[2:3], 0x0
	s_load_dword s1, s[4:5], 0x0
	s_waitcnt lgkmcnt(0)
	v_mov_b32_e32 v2, s1
	v_add_f32_e32 v2, s0, v2
	flat_store_dword v[0:1], v2
	s_exit
	.section	.rodata,#alloc
	.p2align	6
	.kernel fadd
		.group_segment_fixed_size 0
		.private_segment_fixed_size 0
		.user_sgpr_private_segment_buffer 1
		.user_sgpr_dispatch_ptr 0
		.user_sgpr_queue_ptr 0
		.user_sgpr_kernarg_segment_ptr 1
		.user_sgpr_dispatch_id 0
		.user_sgpr_flat_scratch_init 0
		.user_sgpr_private_segment_size 0
		.system_sgpr_private_segment_wavefront_offset 0
		.system_sgpr_workgroup_id_x 1
		.system_sgpr_workgroup_id_y 0
		.system_sgpr_workgroup_id_z 0
		.system_sgpr_workgroup_info 0
		.system_vgpr_workitem_id 0
		.next_free_vgpr 3
		.next_free_sgpr 8
		.reserve_vcc 0
		.reserve_flat_scratch 0
		.float_round_mode_32 0
		.float_round_mode_16_64 0
		.float_denorm_mode_32 3
		.float_denorm_mode_16_64 3
		.dx10_clamp 1
		.ieee_mode 1
		.exception_fp_ieee_invalid_op 0
		.exception_fp_denorm_src 0
		.exception_fp_ieee_div_zero 0
		.exception_fp_ieee_overflow 0
		.exception_fp_ieee_underflow 0
		.exception_fp_ieee_inexact 0
		.exception_int_div_zero 0
	.end_kernel
	.text
.Lfunc_end0:
	.size	fadd, .Lfunc_end0-fadd
                                        ; -- End function
	.section	.AMDGPU.csdata
; Kernel info:
; codeLenInByte = 68
; NumSgprs: 8
; NumVgprs: 3
; ScratchSize: 0
; MemoryBound: 0
; FloatMode: 240
; IeeeMode: 1
; LDSByteSize: 0 bytes/workgroup (compile time only)
; SGPRBlocks: 0
; VGPRBlocks: 0
; NumSGPRsForWavesPerEU: 8
; NumVGPRsForWavesPerEU: 3
; Occupancy: 10
; WaveLimiterHint : 1
; COMPUTE_PGM_RSRC2:SCRATCH_EN: 0
; COMPUTE_PGM_RSRC2:USER_SGPR: 6
; COMPUTE_PGM_RSRC2:TRAP_HANDLER: 0
; COMPUTE_PGM_RSRC2:TGID_X_EN: 1
; COMPUTE_PGM_RSRC2:TGID_Y_EN: 0
; COMPUTE_PGM_RSRC2:TGID_Z_EN: 0
; COMPUTE_PGM_RSRC2:TIDIG_COMP_CNT: 0
	.section	".note.GNU-stack"
	.amdgpu_metadata
---
amdhsa.kernels:
  - .args:
      - .address_space:  global
        .name:           r
        .offset:         0
        .size:           8
        .value_kind:     global_buffer
      - .address_space:  global
        .name:           a
        .offset:         8
        .size:           8
        .value_kind:     global_buffer
      - .address_space:  global
        .name:           b
        .offset:         16
        .size:           8
        .value_kind:     global_buffer
    .group_segment_fixed_size: 0
    .kernarg_segment_align: 8
    .kernarg_segment_size: 24
    .max_flat_workgroup_size: 1024
    .name:           fadd
    .private_segment_fixed_size: 0
    .sgpr_count:     8
    .sgpr_spill_count: 0
    .symbol:         fadd.kd
    .vgpr_count:     3
    .vgpr_spill_count: 0
    .wavefront_size: 64
  - .args:
      - .address_space:  global
        .name:           r
        .offset:         0
        .size:           8
        .value_kind:     global_buffer
      - .address_space:  global
        .name:           a
        .offset:         8
        .size:           8
        .value_kind:     global_buffer
      - .address_space:  global
        .name:           b
        .offset:         16
        .size:           8
        .value_kind:     global_buffer
    .group_segment_fixed_size: 0
    .kernarg_segment_align: 8
    .kernarg_segment_size: 24
    .max_flat_workgroup_size: 1024
    .name:           fsub
    .private_segment_fixed_size: 0
    .sgpr_count:     8
    .sgpr_spill_count: 0
    .symbol:         fsub.kd
    .vgpr_count:     3
    .vgpr_spill_count: 0
    .wavefront_size: 64
  - .args:
      - .name:           i
        .offset:         0
        .size:           4
        .value_kind:     by_value
      - .address_space:  global
        .name:           r
        .offset:         8
        .size:           8
        .value_kind:     global_buffer
      - .address_space:  global
        .name:           a
        .offset:         16
        .size:           8
        .value_kind:     global_buffer
      - .address_space:  global
        .name:           b
        .offset:         24
        .size:           8
        .value_kind:     global_buffer
    .group_segment_fixed_size: 0
    .kernarg_segment_align: 8
    .kernarg_segment_size: 32
    .max_flat_workgroup_size: 1024
    .name:           empty
    .private_segment_fixed_size: 0
    .sgpr_count:     0
    .sgpr_spill_count: 0
    .symbol:         empty.kd
    .vgpr_count:     0
    .vgpr_spill_count: 0
    .wavefront_size: 64
amdhsa.version:
  - 1
  - 0
...

	.end_amdgpu_metadata
