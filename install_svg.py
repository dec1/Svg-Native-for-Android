import os

#from pathLib import PurePath
from pathlib import PurePath
#import pathlib.PurePath
import shutil
import glob



#----------------------------------------------------
tux_dir = "./tux/"
src_dir_jni = tux_dir + "app/src/main/jni/"
src_dir_lib = tux_dir + "app/build/intermediates/ndkBuild/release/obj/local/"

dst_dir = "./install/"
dst_dir_inc = dst_dir + "include/"
dst_dir_lib = dst_dir + "lib/"

abis = ("armeabi", "armeabi-v7a",  "x86", "mips")


include_header_dirs =  ("cairo-*", "glib-*", "*libpng*",  "librsvg-*", "gdk-pixbuf-*")

include_lib_files= ('*tuxpaint_xml2*' ,
                     '*tuxpaint_iconv.*' ,
                     '*tuxpaint_fontconfig.*' ,
                     '*tuxpaint_png.*' ,
                     '*tuxpaint_freetype.*' ,
                     '*tuxpaint_pixman.*' ,
                     '*tuxpaint_cairo.*' ,
                     '*tuxpaint_ffi.*' ,
                     '*SDL2.*' ,
                     '*tp_android_assets_fopen.*' ,
                     '*tuxpaint_intl.*' ,
                     '*tuxpaint_glib.*' ,
                     '*tuxpaint_harfbuzz_ng.*' ,
                     '*tuxpaint_gdk_pixbuf.*' ,
                     '*tuxpaint_pango.*' ,
                     '*tuxpaint_croco.*' ,
                     '*tuxpaint_rsvg.*' )

exclude_header_pattern = ("*.c", "*.cpp", "*.html", "*.png", "*.sgml", "*.xml", "*.jpg", "*.jp2", "*.css", "*.pcf", "*.dat", "*.vcpro*", "*.vcxpro*", "ChangeLog*", "configure",
                          "*.gmo", "*.mo", "*po",  "Makefile", "*.sh" , "NEWS", "*.m4" , "*.txt", "*.cs", "CHANGES", "*.devhelp2", "*.ani", "*.py")


#----------------------------------------------------
# copy all files in src_dir that matches one or more of (glob) patterns in pattern_list to dst_dir
# preserving the (relative) paths (ie each file in a sub dir of src_dir get copied to same sub_dir of dst_dir)
def copy_files_excluding(src_dir, dst_dir, exclude_pattern_list):
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    shutil.copytree(src_dir, dst_dir, ignore=shutil.ignore_patterns(*exclude_pattern_list))
#----------------------------------------------------

# append to src_dirs[] any dir matching pattern passed
def matching_sub_dirs(dir_parent, patterns):
    sub_dirs=[]
    for pattern in patterns:
        matched = glob.glob(dir_parent  + pattern)
        for fp in (d for d in matched if os.path.isdir(d)):
            sub_dirs.extend(matched)
    return sub_dirs
#----------------------------------------------------
# append to src_dirs[] any dir matching pattern passed
def matching_files(dir_parent, patterns):
    files=[]
    for pattern in patterns:
        matched = glob.glob(dir_parent  + pattern)
        for fp in (f for f in matched if os.path.isfile(f)):
            files.extend(matched)
    return files
#----------------------------------------------------

def copy_headers():
    src_dirs = matching_sub_dirs(src_dir_jni, include_header_dirs)

    for src_dir in src_dirs:
        src_dir_name = os.path.basename(src_dir)
        copy_files_excluding(src_dir, dst_dir_inc + src_dir_name, exclude_header_pattern)

# ----------------------------------------------------

def copy_libs():
    #abis = ("armeabi-v7a", "x86")
    lib_src_dir= src_dir_lib

    for abi in abis:
        lib_files = matching_files(lib_src_dir + abi + "/", include_lib_files)
        for file in lib_files:
            dst_dir = dst_dir_lib + abi +"/"
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            shutil.copy2(file, dst_dir)

# ----------------------------------------------------
def clean_libs():
    if os.path.exists(dst_dir_lib):
        shutil.rmtree(dst_dir_lib)
# ----------------------------------------------------      

def clean_headers():
    if os.path.exists(dst_dir_inc):
        shutil.rmtree(dst_dir_inc)
# ----------------------------------------------------  
        
clean_headers()
clean_libs()

copy_headers()
copy_libs()
#----------------------------------------------------
#copy_files_matching("/home/declan/Documents/zone/mid/lib/tux_perepujal/perepujal/install/install/include/cairo-1.14.0/src/", "/home/declan/Documents/zone/low/install_tst/install/headers", ("*.c", "*.cpp"))
#copy_files_matching("/home/declan/Documents/zone/low/install_tst/src/other", "/home/declan/Documents/zone/low/install_tst/install/headers", ("*.c", "*.cpp"))


#
# for header_dir_name in os.listdir(headers_parent_dir):
# #for item in ("cairo-1.14.0", "glib-2.53.3"):
#     header_dir_path = os.path.join(headers_parent_dir, header_dir_name)
#     if os.path.isdir(header_dir_path):
#         if match_any(header_dir_name, header_name_pattern):
#             print(header_dir_name)
#             for relpath, dirs, files in os.walk(header_dir_path):
#                 headers_files = [file for file in files if file.endswith(".h")]
#                 if headers_files:
#                     print(" ----------------------------------")
#                     header_files_rel = ((file, relpath + "/" + file)  for file in headers_files)
#                     #print("headerFiles: \n" +  '\n '.join(header_files_rel))
#                     for file, header_file_rel in header_files_rel:
#                          print("file: " + file + ', rel : ' ' header_file_rel: ' + header_file_rel)
#
#                          pref = PurePath(header_file_rel).relative_to(header_dir_path)
#                          dst_dir = "./install/include/" + str(pref)
#
#                          if not os.path.exists(dst_dir):
#                              os.makedirs(dst_dir)
#                              dst_dir + "/" + file
#
#                          shutil.copy(header_file_rel,  dst_dir)
#             #shutil.cop
#
# exit(0)
#
start = src_dir_lib + "/armeabi-v7a"

for relpath, dirs, files in os.walk(start):
    if relpath.endswith("armeabi-v7a"):
        print(" ----------------------------------")
        print ("relpath: " + relpath)
        print ("dirs: " + ', '.join(dirs))
        print("files: " + ', '.join(files))
    #if name in files:
        #full_path = os.path.join(start, relpath, name)
        #print(os.path.normpath(os.path.abspath(full_path)))


 
