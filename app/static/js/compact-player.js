/**
 * Compact Audio Player
 * A modern lightweight audio player with SoundManager2 integration
 * v1.1.0
 */
const CompactPlayer = (function() {
    let players = [];
    let currentSound = null;
    
    // Main initialization function
    function init() {
        // Check if SoundManager is loaded
        if (typeof soundManager === 'undefined') {
            console.error('SoundManager2 is required for CompactPlayer');
            return;
        }
        
        // Check if SoundManager is ready
        if (soundManager.ok()) {
            initPlayers();
        } else {
            soundManager.onready(initPlayers);
        }
    }
    
    // Initialize all player instances on the page
    function initPlayers() {
        document.querySelectorAll('.compact-player').forEach((playerElement, index) => {
            // Skip already initialized players
            if (playerElement.dataset.initialized === 'true') {
                return;
            }
            
            // Create player object
            const player = {
                element: playerElement,
                id: `compact-player-${index}`,
                url: playerElement.getAttribute('data-url'),
                playButton: playerElement.querySelector('.play-button'),
                progressContainer: playerElement.querySelector('.progress-container'),
                progressBar: playerElement.querySelector('.progress-bar'),
                positionIndicator: playerElement.querySelector('.position-indicator'),
                timeDisplay: playerElement.querySelector('.time'),
                isPlaying: false,
                sound: null
            };
            
            // Skip players without a URL
            if (!player.url) {
                console.error('Compact player missing data-url attribute');
                return;
            }
            
            // Set up event listeners
            player.playButton.addEventListener('click', () => togglePlay(player));
            
            player.progressContainer.addEventListener('click', (e) => {
                if (player.sound) {
                    const rect = player.progressContainer.getBoundingClientRect();
                    const clickPosition = (e.clientX - rect.left) / rect.width;
                    const duration = player.sound.durationEstimate || player.sound.duration;
                    player.sound.setPosition(clickPosition * duration);
                }
            });
            
            // Create the sound object
            player.sound = soundManager.createSound({
                id: player.id,
                url: player.url,
                autoLoad: true,
                autoPlay: false,
                whileplaying: () => updateProgress(player),
                onfinish: () => resetPlayer(player),
                onload: (success) => {
                    if (!success) {
                        console.error(`Failed to load sound: ${player.url}`);
                        player.element.classList.add('load-error');
                    }
                }
            });
            
            // Mark as initialized
            playerElement.dataset.initialized = 'true';
            
            // Add to player collection
            players.push(player);
        });
    }
    
    // Toggle play/pause state
    function togglePlay(player) {
        if (player.isPlaying) {
            pauseSound(player);
        } else {
            playSound(player);
        }
    }
    
    // Start playing a sound
    function playSound(player) {
        // Pause currently playing sound
        if (currentSound && currentSound !== player.sound) {
            currentSound.pause();
            players.forEach((p) => {
                if (p.sound === currentSound) {
                    p.isPlaying = false;
                    p.element.classList.remove('playing');
                    p.playButton.innerHTML = '<i class="icon icon-play"></i>';
                }
            });
        }
        
        // Play this sound
        player.sound.play();
        player.isPlaying = true;
        player.element.classList.add('playing');
        player.playButton.innerHTML = '<i class="icon icon-pause"></i>';
        currentSound = player.sound;
    }
    
    // Pause a sound
    function pauseSound(player) {
        player.sound.pause();
        player.isPlaying = false;
        player.element.classList.remove('playing');
        player.playButton.innerHTML = '<i class="icon icon-play"></i>';
    }
    
    // Reset player to initial state
    function resetPlayer(player) {
        player.isPlaying = false;
        player.element.classList.remove('playing');
        player.playButton.innerHTML = '<i class="icon icon-play"></i>';
        player.progressBar.style.width = '0%';
        player.positionIndicator.style.right = '0%';
        player.timeDisplay.textContent = `0:00 / ${formatTime(player.sound.duration)}`;
    }
    
    // Update progress display
    function updateProgress(player) {
        const position = player.sound.position;
        const duration = player.sound.durationEstimate || player.sound.duration;
        
        if (!duration) return;
        
        const progress = (position / duration) * 100;
        
        player.progressBar.style.width = `${progress}%`;
        player.positionIndicator.style.right = `${progress}%`;
        player.timeDisplay.textContent = `${formatTime(position)} / ${formatTime(duration)}`;
    }
    
    // Format milliseconds to MM:SS
    function formatTime(ms) {
        if (!ms || isNaN(ms)) return '0:00';
        
        const totalSeconds = Math.floor(ms / 1000);
        const minutes = Math.floor(totalSeconds / 60);
        const seconds = totalSeconds % 60;
        
        return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    }
    
    // Public API
    return {
        init: init,
        getPlayers: () => players
    };
})();

// Initialize using both modern and legacy approaches
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', CompactPlayer.init);
} else {
    // DOM already loaded, initialize immediately
    CompactPlayer.init();
}

// Also support jQuery if available
if (typeof jQuery !== 'undefined') {
    jQuery(document).ready(function() {
        CompactPlayer.init();
    });
} 