public class FileHandler {
    public List<File> getFiles(FileSet fileSet) {
        List<File> files = new ArrayList<>();
        String[] names = fileSet.getDirectoryScanner(project).getIncludedFiles();

        for (int i = 0; i < names.length; i++) {
            String name = names[i];
            files.add(new File(fileSet.getDir(project), name));
        }
        return files;
    }
}