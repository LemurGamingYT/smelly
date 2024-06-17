#pragma once

#ifdef __cplusplus
extern "C" {
#endif


#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>


#if defined(_WIN32) || defined(_WIN64)
    #define OS_WINDOWS
    #ifndef WIN32_LEAN_AND_MEAN
        #define WIN32_LEAN_AND_MEAN
    #endif
    #ifndef NOMINMAX
        #define NOMINMAX
    #endif
    #include <windows.h>
#elif defined(__APPLE__)
    #define OS_MAC
#elif defined(__linux__)
    #define OS_LINUX
    #include <unistd.h>
#else
    #define OS_UNKNOWN
#endif

#if defined(_M_X64)
    #define ARCH_x86_64
#elif defined(_M_IX86)
    #define ARCH_x86
#elif defined(_M_ARM64)
    #define ARCH_arm64
#else
    #define ARCH_unknown
#endif


#define MIN_INT -2147483648
#define MAX_INT 2147483647

#define ONE_BILLION 1000000000
#define ONE_MILLION 1000000
#define ONE_THOUSAND 1000

#define DIGITS "0123456789"
#define ASCII_LOWER "abcdefghijklmnopqrstuvwxyz"
#define ASCII_UPPER "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#define ASCII_LETTERS "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#define PUNCTUATION " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
#define HEXDIGITS "0123456789ABCDEF"

#define VERSION "0.0.1"


#define err(msg) printf("error: %s\n", msg); exit(1);
#define buffer_creation_check(buf) if (buf == NULL) { err("out of memory") }


typedef struct { unsigned char _; } Math;
typedef struct { unsigned char _; } System;


typedef void* nil;
typedef char* string;


/*returns: string*/
#define int_type() "int"

/*returns: string*/
#define float_type() "float"

/*returns: string*/
#define string_type() "string"

/*returns: string*/
#define bool_type() "bool"

/*returns: string*/
#define nil_type() "nil"

/*returns: string*/
#define Math_type() "Math"


/*params: i:int
attrs: free*/
static string int_repr(const int i) {
    string buf = (string)malloc(sizeof(i) + 1);
    buffer_creation_check(buf)
    snprintf(buf, sizeof(buf), "%d", i);
    return buf;
}

/*params: f:float
attrs: free*/
static string float_repr(const float f) {
    string buf = (string)malloc(sizeof(f) + 1);
    buffer_creation_check(buf)
    snprintf(buf, sizeof(buf), "%f", f);
    return buf;
}

/*params: s:string
returns: string*/
#define string_repr(s) s

/*params: b:bool
returns: string*/
#define bool_repr(b) (b ? "true" : "false")

/*params: n:nil
returns: string*/
#define nil_repr(n) "nil"

/*params: m:Math
returns: string*/
#define Math_repr(m) "class 'Math'"


/*params: b:bool
returns: bool*/
#define bool_bool(b) b


/*params: x:int, y:int
returns: int*/
#define int_add_int(x, y) (x+y)

/*params: x:float, y:int
returns: float*/
#define float_add_int(x, y) (x+(float)y)

/*params: x:int, y:float
returns: float*/
#define int_add_float(x, y) ((float)x+y)

/*params: x:float, y:float
returns: float*/
#define float_add_float(x, y) (x+y)

/*params: x:string, y: string
attrs: free*/
static string string_add_string(const string x, const string y) {
    string res = (string)malloc(strlen(x) + strlen(y) + 1);
    buffer_creation_check(res)
    strcpy(res, x);
    strcat(res, y);
    return res;
}


/*params: x:int, y:int
returns: int*/
#define int_sub_int(x, y) (x-y)

/*params: x:float, y:int
returns: float*/
#define float_sub_int(x, y) (x-(float)y)

/*params: x:int, y:float
returns: float*/
#define int_sub_float(x, y) ((float)x-y)

/*params: x:float, y:float
returns: float*/
#define float_sub_float(x, y) (x-y)


/*params: x:int, y: int
returns: int*/
#define int_mul_int(x, y) (x*y)

/*params: x:float, y:int
returns: float*/
#define float_mul_int(x, y) (x*(float)y)

/*params: x:int, y:float
returns: float*/
#define int_mul_float(x, y) ((float)x*y)

/*params: x:float, y:float
returns: float*/
#define float_mul_float(x, y) (x*y)


/*params: x:int, y:int
returns: float*/
#define int_div_int(x, y) (x/y)

/*params: x:float, y:int
returns: float*/
#define float_div_int(x, y) (x/(float)y)

/*params: x:int, y:float
returns: float*/
#define int_div_float(x, y) ((float)x/y)

/*params: x:float, y:float
returns: float*/
#define float_div_float(x, y) (x/y)


/*params: x:int, y:int
returns: int*/
#define int_mod_int(x, y) (x%y)

/*params: x: float, y:int
returns: float*/
#define float_mod_int(x, y) fmod(x, (float)y)

/*params: x:int, y:float
returns: float*/
#define int_mod_float(x, y) fmod((float)x, y)

/*params: x:float, y:float
returns: float*/
#define float_mod_float(x, y) fmod(x, y)


/*params: x:int, y:int
returns: bool*/
#define int_eq_int(x, y) (x==y)

/*params: x:float, y:int
returns: bool*/
#define float_eq_int(x, y) (x==(float)y)

/*params: x:int, y:float
returns: bool*/
#define int_eq_float(x, y) ((float)x==y)

/*params: x:float, y:float
returns: bool*/
#define float_eq_float(x, y) (x==y)

/*params: x:string, y:string
returns: bool*/
#define string_eq_string(x, y) (strcmp(x, y) == 0)

/*params: x:bool, y:bool
returns: bool*/
#define bool_eq_bool(x, y) (x==y)


/*params: x:int, y:int
returns: bool*/
#define int_neq_int(x, y) (x!=y)

/*params: x:float, y:int
returns: bool*/
#define float_neq_int(x, y) (x!=(float)y)

/*params: x:int, y:float
returns: bool*/
#define int_neq_float(x, y) ((float)x!=y)

/*params: x:float, y:float
returns: bool*/
#define float_neq_float(x, y) (x!=y)

/*params: x:string, y:string
returns: bool*/
#define string_neq_float(x, y) (strcmp(x, y) != 0)

/*params: x:bool, y:bool
returns: bool*/
#define bool_neq_bool(x, y) (x!=y)


/*params: x:int, y:int
returns: bool*/
#define int_gt_int(x, y) (x>y)

/*params: x:float, y:int
returns: bool*/
#define float_gt_int(x, y) (x>(float)y)

/*params: x:int, y:float
returns: bool*/
#define int_gt_float(x, y) ((float)x>y)

/*params: x:float, y:float
returns: bool*/
#define float_gt_float(x, y) (x>y)

/*params: x:string, y:string
returns: bool*/
#define string_gt_string(x, y) (strlen(x)>strlen(y))


/*params: x:int, y:int
returns: bool*/
#define int_lt_int(x, y) (x<y)

/*params: x:float, y:int
returns: bool*/
#define float_lt_int(x, y) (x<(float)y)

/*params: x:int, y:float
returns: bool*/
#define int_lt_float(x, y) ((float)x<y)

/*params: x:float, y:float
returns: bool*/
#define float_lt_float(x, y) (x<y)

/*params: x:string, y:string
returns: bool*/
#define string_lt_string(x, y) (strlen(x) < strlen(y))


/*params: x:int, y:int
returns: bool*/
#define int_gte_int(x, y) (x>=y)

/*params: x:float, y:int
returns: bool*/
#define float_gte_int(x, y) (x>=(float)y)

/*params: x:int, y:float
returns: bool*/
#define int_gte_float(x, y) ((float)x>=y)

/*params: x:float, y:float
returns: bool*/
#define float_gte_float(x, y) (x>=y)

/*params: x:string, y:string
returns: bool*/
#define string_gte_string(x, y) (strlen(x)>=strlen(y))


/*params: x:int, y:int
returns: bool*/
#define int_lte_int(x, y) (x<=y)

/*params: x:float, y:int
returns: bool*/
#define float_lte_int(x, y) (x<=(float)y)

/*params: x:int, y:float
returns: bool*/
#define int_lte_float(x, y) ((float)x<=y)

/*params: x:float, y:float
returns: bool*/
#define float_lte_float(x, y) (x<=y)

/*params: x:string, y:string
returns: bool*/
#define string_lte_string(x, y) (strlen(x)<=strlen(y))


/*params: x:bool, y:bool
returns: bool*/
#define bool_and_bool(x, y) (x&&y)


/*params: x:bool, y:bool
returns: bool*/
#define bool_or_bool(x, y) (x||y)


/*params: x:bool
returns: bool*/
#define not_bool(b) (!b)


/*params: x:any
returns: int*/
#define print(x) printf("%s\n", x)


/*params: s:string
returns: int
attrs: property*/
#define string_length(s) (strlen(s))

/*params: s:string
attrs: property*/
static bool string_is_digit(const string s) {
    for (int i = 0; i < strlen(s); i++) {
        if (!isdigit(s[i])) return false;
    }

    return true;
}

/*params: s:string
attrs: property*/
static bool string_is_alpha(const string s) {
    for (int i = 0; i < strlen(s); i++) {
        if (!isalpha(s[i])) return false;
    }

    return true;
}

/*params: s:string
attrs: property*/
static bool string_is_space(const string s) {
    for (int i = 0; i < strlen(s); i++) {
        if (!isspace(s[i])) return false;
    }

    return true;
}

/*params: s:string
returns: bool
attrs: property*/
#define string_is_empty(s) (strlen(s) == 0)

/*params: s:string
returns: bool
attrs: property*/
#define string_parse_int(s) (atoi(s))

/*params: s:string
returns: bool
attrs: property*/
#define string_parse_float(s) (atof(s))

/*params: s:string
returns: bool
attrs: property*/
#define string_parse_bool(s) (s == "true")

/*params: s:string
returns: bool
attrs: property*/
#define string_parse_nil(s) NULL

/*params: s:string
attrs: method*/
static string string_lower(const string s) {
    string res = (string)malloc(strlen(s) + 1);
    buffer_creation_check(res);
    for (int i = 0; i < strlen(s); i++) {
        res[i] = tolower(s[i]);
    }
    res[strlen(s)] = '\0';

    return res;
}

/*params: s:string, prefix:string
returns: bool
attrs: method*/
#define string_startswith(s, prefix) (strncmp(s, prefix, strlen(prefix)) == 0)

/*params: s:string, prefix:string
attrs: method*/
static bool string_endswith(const string s, const string suffix) {
    size_t slen = strlen(s);
    size_t sulen = strlen(suffix);
    if (slen < sulen) return 0;
    return strncmp(s + slen - sulen, suffix, sulen) == 0;
}

/*params: s:string, character:string
attrs: method*/
static int string_index_of(const string s, const string character) {
    if (strlen(character) < 1 || strlen(character) > 1) {
        err("Character must be a single character")
    }

    char c = character[0];
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] == c) return i;
    }

    return -1;
}

/*params: s:string, character:string
attrs: method*/
static int string_last_index_of(const string s, const string character) {
    if (strlen(character) < 1 || strlen(character) > 1) {
        err("Character must be a single character")
    }

    char c = character[0];
    for (int i = strlen(s); i >= 0; i--) {
        if (s[i] == c) return i;
    }

    return -1;
}

/*params: s:string, i:int
attrs: method free*/
static string string_at(const string s, const int i) {
    if (i > strlen(s) - 1) {
        err("Index out of bounds on string")
    }

    string buf = (string)malloc(2);
    buffer_creation_check(buf);
    buf[0] = s[i];
    buf[1] = '\0';
    return buf;
}

/*params: s:string, substring:string
returns: bool
attrs: method*/
static bool string_has(const string s, const string substring) {
    string copy = (string)malloc(strlen(s) + 1);
    buffer_creation_check(copy)
    strncpy(copy, s, strlen(s) + 1);

    bool res = strstr(copy, substring) != NULL;
    free(copy);
    return res;
}

/*params: s:string, n:int
returns: string
attrs: method free*/
static string string_repeat(const string s, const int n) {
    if (n <= 0) return "";
    if (n == 1) return s;

    string res = s;
    for (int i = 0; i < n; i++) {
        res = string_add_string(res, s);
    }

    return res;
}

/*params: s:string, start:int, end:int
returns: string
attrs: method free*/
static string string_slice(const string s, const int start, const int end) {
    if (start < 0 || end < 0) {
        err("Index out of bounds on string slice")
    }

    if (start > end) {
        err("Start index is greater than end index on string slice")
    }

    string buf = (string)malloc(end - start + 1);
    buffer_creation_check(buf)
    strncpy(buf, s + start, end - start + 1);
    buf[end - start + 1] = '\0';
    return buf;
}

/*params: s:string, character:string
returns: string
attrs: method*/
static string string_remove(const string s, const string character) {
    if (strlen(character) < 1 || strlen(character) > 1) {
        err("Character to remove must be a single character")
    }

    string buf = strdup(s);
    buffer_creation_check(buf)

    char c = character[0];
    for (int i = 0; i < strlen(buf); i++) {
        if (buf[i] == c) {
            for (int j = i; j < strlen(buf) - 1; j++) {
                buf[j] = buf[j + 1];
            }

            buf[strlen(buf) - 1] = '\0';
        }
    }

    return buf;
}


/*returns: float
attrs: static property*/
#define Math_pi() 3.14159265358979323846f

/*returns: float
attrs: static property*/
#define Math_e() 2.71828182845904523536f

/*params: x:float
returns: float
attrs: static method*/
#define Math_sin(x) ((float)sin(x))

/*params: x:float
returns: float
attrs: static method*/
#define Math_cos(x) ((float)cos(x))

/*params: x:float
returns: float
attrs: static method*/
#define Math_tan(x) ((float)tan(x))

/*params: x:float
returns: float
attrs: static method*/
#define Math_asin(x) ((float)asin(x))

/*params: x:float
returns: float
attrs: static method*/
#define Math_acos(x) ((float)acos(x))

/*params: x:float
returns: float
attrs: static method*/
#define Math_atan(x) ((float)atan(x))

/*params: x:float, y:float
returns: float
attrs: static method*/
#define Math_atan2(x, y) ((float)atan2(y, x))

/*params: x:float
returns: int
attrs: static method*/
#define Math_floor(x) ((int)floor(x))

/*params: x:float
returns: int
attrs: static method*/
#define Math_ceil(x) ((int)ceil(x))

/*params: x:float
returns: float
attrs: static method*/
#define Math_log(x) ((float)log(x))

/*params: x:float
returns: float
attrs: static method*/
#define Math_log10(x) ((float)log10(x))

/*params: x:float
returns: float
attrs: static method*/
#define Math_abs(x) ((float)fabs(x))

/*params: base:float, exponent:float
returns: float
attrs: static method*/
#define Math_pow(base, exponent) ((float)pow(base, exponent))

/*params: a:float, b:float
returns: int
attrs: static method*/
#define Math_floor_div(a, b) ((int)floor(a / b))

/*params: a:float, b:float
returns: float
attrs: static method*/
#define Math_min(a, b) a < b ? a : b

/*params: a:float, b:float
returns: float
attrs: static method*/
#define Math_max(a, b) a < b ? b : a


/*returns: string
attrs: static property*/
static string System_os() {
#ifdef OS_WINDOWS
    return "Windows";
#elif defined(OS_MAC)
    return "Mac";
#elif defined(OS_LINUX)
    return "Linux";
#else
    return "Unknown";
#endif
}

/*returns: string
attrs: static property*/
static string System_arch() {
#ifdef ARCH_x86_64
    return "x86_64";
#elif ARCH_x86
    return "x86";
#elif ARCH_arm64
    return "arm64";
#else
    return "Unknown";
#endif
}

/*params: key:string
attrs: static method*/
static string System_env(const string key) {
    string value = NULL;
    size_t len;
    _dupenv_s(&value, &len, key);
    return value;
}

/*params: code:int
attrs: static method*/
static nil System_exit(const int code) {
    exit(code);
    return NULL;
}

/*params: seconds:float
attrs: static method*/
static nil System_sleep(const float seconds) {
#ifdef OS_WINDOWS
    Sleep(seconds * 1000);
#else
    err("System.sleep() not supported on this device")
#endif
    return NULL;
}

/*params: command:string
attrs: static method free*/
static string System_run(const string command) {
    char buf[128];
    FILE* pipe = _popen(command, "r");
    if (!pipe) {
        err("Opening pipe failed")
    }

    string res = (string)malloc(sizeof(char));
    res[0] = '\0';

    while (fgets(buf, sizeof(buf), pipe) != NULL) {
        res = realloc(res, strlen(res) + strlen(buf) + 1);
        strcat(res, buf);
    }

    _pclose(pipe);
    return res;
}


#ifdef __cplusplus
}
#endif
