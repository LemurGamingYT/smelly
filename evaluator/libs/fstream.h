#pragma once

#ifdef __cplusplus
extern "C" {
#endif


#include "../compiler.h"


typedef struct {
    FILE* fp;
    string mode;
    string path;
} File;


/*params: path:string, mode:string
attrs: function*/
File* open(const string path, const string mode) {
    File* file = (File*)malloc(sizeof(File));
    fopen_s(&file->fp, path, mode);
    file->mode = _strdup(mode);
    file->path = _strdup(path);
    return file;
}

/*params: path:string
attrs: function*/
static bool exists(const string path) {
#ifdef OS_WINDOWS
    DWORD attrs = GetFileAttributesA(path);
    return attrs != INVALID_FILE_ATTRIBUTES;
#else
    err("fstream.exists() not supported on this device")
#endif
}

/*params: path:string
attrs: function*/
static bool delete(const string path) {
#ifdef OS_WINDOWS
    return DeleteFileA(path);
#else
    err("fstream.delete() not supported on this device")
#endif
}

/*params: old_path:string, new_path:string
attrs: function*/
static bool rename(const string old_path, const string new_path) {
    return MoveFileA(old_path, new_path);
}

/*params: path:string
attrs: function*/
static bool create_dir(const string path) {
#ifdef OS_WINDOWS
    return CreateDirectoryA(path, NULL);
#else
    err("fstream.create_dir() not supported on this device")
#endif
}

/*params: path:string
attrs: function*/
static bool remove_dir(const string path) {
#ifdef OS_WINDOWS
    return RemoveDirectoryA(path);
#else
    err("fstream.remove_dir() not supported on this device")
#endif
}


/*params: f:File
returns: string
attrs: property*/
#define File_path(f) f->path

/*params: f:File
returns: string
attrs: property*/
#define File_mode(f) f->mode

/*params: f:File
attrs: property free*/
static string File_contents(const File* f) {
    fseek(f->fp, 0, SEEK_END);
    long size = ftell(f->fp);
    rewind(f->fp);

    string buf = (string)malloc(size + 1);
    buffer_creation_check(buf)

    size_t bytesRead = fread(buf, 1, size, f->fp);
    if (bytesRead != size) {
        free(buf);
        err("Error reading file")
    }

    buf[bytesRead] = '\0';
    return buf;
}

/*params: f:File
attrs: method*/
static nil File_close(File* f) {
    fclose(f->fp);
    free(f->mode);
    free(f);
}


#ifdef __cplusplus
}
#endif
