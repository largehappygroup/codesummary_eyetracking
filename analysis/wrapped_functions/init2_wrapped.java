public class InitClass {
    private void init() throws CoreException {
        final String name = getClassName();
        final IPackageFragment pkg = getPackage();
        final ICompilationUnit unit = pkg.createCompilationUnit(name + ".java", "", true, null);
        setUp(unit);
        createMainType(PUBLIC_KEYWORD, pkg.getElementName(), getClassName());
    }
}