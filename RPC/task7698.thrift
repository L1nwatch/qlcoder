namespace cpp qlcoder
namespace d qlcoder
namespace java qlcoder
namespace php qlcoder
namespace perl qlcoder
namespace haxe qlcoder

enum Type {
  GET_ANSWER = 1,
  GET_CREATEDTIME = 2,
  GET_AUTHOR = 3,
}

struct Auth {
  1: string username,
  2: Type type,
}

service Task {
   string getTaskInfo(1:Auth auth),
}
