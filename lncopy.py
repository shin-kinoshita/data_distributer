import os
import shutil
import ConfigParser

def lncopy(in_dir_path, out_dir_path, class_dic):
    train_class_list = [ class_name for class_name in os.listdir(in_dir_path)
                        if os.path.isdir(in_dir_path + '/' + class_name)]

    for train_class_name in train_class_list:
        os.mkdir(out_dir_path + '/' + train_class_name)
        os.mkdir(out_test_dir_path + '/' + train_class_name)

        test_class_name = class_dic[train_class_name]

        # copy train files
        for file_name in os.listdir(in_dir_path + '/' + train_class_name):
            in_file_path  = in_dir_path + '/' + train_class_name + '/' + file_name
            out_file_path = out_dir_path + '/' + train_class_name + '/' + file_name
            shutil.copyfile(in_file_path, out_file_path)
        
        # copy test files
        for file_name in os.listdir(in_test_dir_path + '/' + test_class_name):
            in_file_path  = in_test_dir_path + '/' + test_class_name + '/' + file_name
            out_file_path = out_test_dir_path + '/' + train_class_name + '/' + file_name
            shutil.copyfile(in_file_path, out_file_path)

if __name__ == '__main__':
    config_path = sys.argv[1]
    config = ConfigParser.SafeConfigParser()
    config.read(config_path)

    in_dir_path = config.get('directory', 'train_dir')
    out_dir_path = config.get('directory', 'test_dir')
    class_dic = {}
    for class_pair in config.items('class_pair'):
        train_class = class_pair[0]
        test_class  = class_pair[1]
        class_dic[train_class] = test_class

    lncopy(in_dir_path, out_dir_path, class_dic)

