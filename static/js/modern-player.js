/**
 * Modern Audio Player
 * A lightweight audio player based on Howler.js with RTL support
 * v1.1.0
 */
const ModernPlayer = (function() {
    let players = [];
    let currentSound = null;
    let isRtl = document.documentElement.dir === 'rtl';
    
    // Main initialization function
    function init() {
        // Check if Howler is loaded
        if (typeof Howl === 'undefined') {
            console.error('Howler.js is required for ModernPlayer');
            return;
        }
        
        // Initialize all players on the page
        document.querySelectorAll('.compact-player').forEach((playerElement, index) => {
            // Skip already initialized players
            if (playerElement.dataset.initialized === 'true') {
                return;
            }
            
            const audioUrl = playerElement.getAttribute('data-url');
            if (!audioUrl) {
                console.error('Audio player missing data-url attribute');
                return;
            }
            
            // Create player object
            const player = {
                element: playerElement,
                id: `player-${index}`,
                url: audioUrl,
                playButton: playerElement.querySelector('.play-button'),
                progressContainer: playerElement.querySelector('.progress-container'),
                progressBar: playerElement.querySelector('.progress-bar'),
                positionIndicator: playerElement.querySelector('.position-indicator'),
                timeDisplay: playerElement.querySelector('.time'),
                isPlaying: false,
                sound: null,
                duration: 0,
                seek: null
            };
            
            // Initialize Howl for this player
            player.sound = new Howl({
                src: [player.url],
                html5: true, // Use HTML5 Audio for streaming
                preload: true,
                onload: function() {
                    player.duration = player.sound.duration();
                    player.timeDisplay.textContent = `0:00 / ${formatTime(player.duration)}`;
                },
                onplay: function() {
                    requestAnimationFrame(() => updateProgress(player));
                },
                onend: function() {
                    resetPlayer(player);
                },
                onloaderror: function() {
                    console.error(`Failed to load sound: ${player.url}`);
                    player.element.classList.add('load-error');
                }
            });
            
            // Set up event listeners
            player.playButton.addEventListener('click', () => togglePlay(player));
            
            player.progressContainer.addEventListener('click', (e) => {
                const rect = player.progressContainer.getBoundingClientRect();
                // Handle RTL layout for progress bar clicks
                const clickPosition = isRtl 
                    ? 1 - ((e.clientX - rect.left) / rect.width)
                    : (e.clientX - rect.left) / rect.width;
                
                const seekPosition = player.duration * clickPosition;
                player.sound.seek(seekPosition);
                updateProgress(player);
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
                    p.playButton.innerHTML = '<i class="fa-solid fa-play"></i>';
                }
            });
        }
        
        // Play this sound
        player.sound.play();
        player.isPlaying = true;
        player.element.classList.add('playing');
        player.playButton.innerHTML = '<i class="fa-solid fa-pause"></i>';
        currentSound = player.sound;
    }
    
    // Pause a sound
    function pauseSound(player) {
        player.sound.pause();
        player.isPlaying = false;
        player.element.classList.remove('playing');
        player.playButton.innerHTML = '<i class="fa-solid fa-play"></i>';
    }
    
    // Reset player to initial state
    function resetPlayer(player) {
        player.isPlaying = false;
        player.element.classList.remove('playing');
        player.playButton.innerHTML = '<i class="fa-solid fa-play"></i>';
        player.progressBar.style.width = '0%';
        player.positionIndicator.style.right = '0%';
        player.timeDisplay.textContent = `0:00 / ${formatTime(player.duration)}`;
    }
    
    // Update progress display (called on animation frame)
    function updateProgress(player) {
        if (player.isPlaying) {
            const seek = player.sound.seek() || 0;
            const duration = player.duration;
            
            if (duration > 0) {
                const progress = (seek / duration) * 100;
                
                // Update progress bar
                player.progressBar.style.width = `${progress}%`;
                
                // Update position indicator for RTL layout
                if (isRtl) {
                    player.positionIndicator.style.left = `${progress}%`;
                    player.positionIndicator.style.transform = 'translateX(-50%)';
                } else {
                    player.positionIndicator.style.right = `${progress}%`;
                }
                
                // Use Arabic locale for time display if available
                if (typeof moment !== 'undefined' && moment.locale() === 'ar') {
                    const seekTime = moment.duration(seek, 'seconds').format('m:ss');
                    const durationTime = moment.duration(duration, 'seconds').format('m:ss');
                    player.timeDisplay.textContent = `${seekTime} / ${durationTime}`;
                } else {
                    player.timeDisplay.textContent = `${formatTime(seek)} / ${formatTime(duration)}`;
                }
            }
            
            // Continue updating while playing
            requestAnimationFrame(() => updateProgress(player));
        }
    }
    
    // Format seconds to MM:SS
    function formatTime(seconds) {
        if (!seconds || isNaN(seconds)) return '0:00';
        
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = Math.floor(seconds % 60);
        
        return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
    }
    
    // Public API
    return {
        init: init,
        getPlayers: () => players,
        isRtl: isRtl
    };
})();

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ModernPlayer.init);
} else {
    // DOM already loaded, initialize immediately
    ModernPlayer.init();
}

// Also support jQuery if available
if (typeof jQuery !== 'undefined') {
    jQuery(document).ready(function() {
        ModernPlayer.init();
    });
} 