public class RodinDBStatusParser {

    public IRodinDBStatus getRodinDBStatus() {
        IStatus status = this.getStatus();

        if (status instanceof IRodinDBStatus) {
            return (IRodinDBStatus) status;
        } else {
            // A regular IStatus is created only in the case of a CoreException.
            // See bug 13492 Should handle RodinDBExceptions that contains
            // CoreException more gracefully
            return new RodinDBStatus(this.nestedCoreException);
        }
    }
}