#pragma once

enum class opu_op_t {
  NO_OP = -1
  {{OpTypeList}}
};

enum class opu_atomic_t {
  INVALID = -1
  {{OpAtomicList}}
};

enum class opu_datatype_t {
  INVALID = -1
  {{DataTypeList}}
};

enum class opu_cacheop_t {
  INVALID = -1
  {{CacheOpList}}
};

enum class opu_mspace_t {
  {{MSpaceList}}
};

enum class opu_memop_t {
  {{MemopList}}
};

