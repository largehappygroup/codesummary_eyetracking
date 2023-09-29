public class ViewRemover {
    public void removeView(StateViewSmall view) {
        view.setVisible(false);
        // remove from scenario
        int removedPosition = indexOfView(view);
        mScenarioPanel.remove(removedPosition);
        // take care of the big ( detailed ) view

        if (mCurrentSmallView != null && mCurrentSmallView.equals(view)) {
            mCurrentBigView.setVisible(false);
            mCurrentBigView = null;
            mCurrentSmallView = null;
        }
        // compute the new number of pixels per scenario position
        mTimeBar.scaleNumberOfPixelsPerPosition();
        refresh();
    }
}