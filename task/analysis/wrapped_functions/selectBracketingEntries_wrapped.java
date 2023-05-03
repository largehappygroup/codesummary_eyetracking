public class Wrapper {

    protected boolean selectBracketingEntries(final AbsoluteDate date) {
        try {
            // select the bracketing elements
            next = (TimeStampedEntry) (eop.tailSet(date).first());
            previous = (TimeStampedEntry) (eop.headSet(next).last());
            return true;
        } catch (NoSuchElementException nsee) {
            previous = null;
            next = null;
            return false;
        }
    }
}