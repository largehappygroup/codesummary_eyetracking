public class TimerClass {
    private Map<Object, Long> pair2startTimeMap;
    private Clock clock;
    private int maxWait;

    public TimerClass() {
        pair2startTimeMap = new HashMap<>();
        clock = new Clock();
        maxWait = 1000;
    }

    public void markStart(Object tag) {
        synchronized (pair2startTimeMap) {
            pair2startTimeMap.put(tag, clock.getCurrentTime());
            Timer removalTimer = clock.createNewTimer();
            removalTimer.addTimerListener(new GarbageCollectionTimerListener(tag));
            removalTimer.schedule(Time.inMilliseconds(maxWait));
        }
    }

    private class GarbageCollectionTimerListener implements TimerListener {
        Object tag;

        public GarbageCollectionTimerListener(Object tag) {
            this.tag = tag;
        }

        @Override
        public void onTimerExpired() {
            synchronized (pair2startTimeMap) {
                pair2startTimeMap.remove(tag);
            }
        }
    }

    private interface TimerListener {
        void onTimerExpired();
    }

    private static class Timer {
        private TimerListener listener;

        public void addTimerListener(TimerListener listener) {
            this.listener = listener;
        }

        public void schedule(int time) {
            // No-op for demo purposes
        }
    }

    private static class Time {
        public static int inMilliseconds(int seconds) {
            return seconds * 1000;
        }
    }

    private static class Clock {
        public long getCurrentTime() {
            return System.currentTimeMillis();
        }

        public Timer createNewTimer() {
            return new Timer();
        }
    }
}