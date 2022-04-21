	.text
	;.amdgcn_target "amdgcn-amd-amdhsa--gfx803"
	.globl	hello                            ; -- Begin function hello
	.p2align	8
	.type	hello,@function
hello:                                   ; @hello
; %bb.0:                                ; %entry
    v_load_dwordx2 s[0:1], param0, 0x0 % mspace:param
   	v_load_dwordx2 s[2:3], param1, 0x2 - mspace:param
	v_lshlrev_b32 v0, 2, v0
    s_waitcnt 0

	// v[1:2] = &in1[i]
	v_add_u32     v1, s0, v0, co:tcc0
   	v_mov_b32     v2, s1
	v_addc_u32    v2, 0, v2, ci:tcc0, co:tcc0
	flat_load_dword v3, v[1:2] // v3 = in1[i]

	// v[0:1] = &out[i]
	v_add_u32     v0, s2, v0, co:tcc0
	v_mov_b32     v1, s3
	v_addc_u32    v1, 0, v1, ci:tcc0, co:tcc0

	s_waitcnt     0

	v_mov_b32      v4, v3 // v3 = in1[i]

    flat_store_dword v[0:1], v4
	s_exit
	.section	.rodata,#alloc
	.p2align	6
	.kernel hello
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
		.reserve_tcc0 0
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
	.size	hello, .Lfunc_end0-hello
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
        .name:           param0
        .offset:         0
        .size:           8
        .value_kind:     global_buffer
      - .address_space:  global
        .name:           param1
        .offset:         8
        .size:           8
        .value_kind:     global_buffer
      - .address_space:  global
        .name:           param2
        .offset:         16
        .size:           8
        .value_kind:     global_buffer
    .group_segment_fixed_size: 0
    .kernarg_segment_align: 8
    .kernarg_segment_size: 24
    .max_flat_workgroup_size: 1024
    .name:           hello
    .private_segment_fixed_size: 0
    .sgpr_count:     8
    .sgpr_spill_count: 0
    .symbol:         hello.kd
    .vgpr_count:     3
    .vgpr_spill_count: 0
    .wavefront_size: 64
amdhsa.version:
  - 1
  - 0
...

	.end_amdgpu_metadata
