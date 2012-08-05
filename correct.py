import os

# os.chdir('ideas.okfn.org/ideas')
os.chdir('getthedata.org/questions')
for dirpath, dirnames, filenames in os.walk('.'):
    if len(dirpath) > 3 and (dirpath[2] in '0123456789'):
        if len(dirnames) == 0:
            # /287/xyz versus /287/xyz/123
            if len(dirpath.split('/')) == 2:
                newdir = os.path.join(dirpath, filenames[0])
                tmp = newdir + '.html'
                dest = os.path.join(newdir, 'index.html')
                print 1, newdir, dest
                # print 1, newdir
                os.rename(newdir, tmp)
                os.makedirs(newdir)
                os.rename(tmp, dest)
            else:
                filepath = os.path.join(dirpath, filenames[0])
                dest = os.path.join(dirpath, 'index.html')
                print 2, dirpath, dest
                os.rename(filepath, dest)
                for fn in filenames[1:]:
                    os.remove(os.path.join(dirpath, fn))
                # print dirpath, filenames

