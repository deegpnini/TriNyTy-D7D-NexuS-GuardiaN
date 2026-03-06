"""
Vibrational Analysis Service

Implements vibrational frequency analysis using signal processing techniques.
Analyzes time-series data (voice, biometric, etc.) to extract:
- Dominant frequencies
- Harmonic patterns
- Resonance qualities

Uses numpy and scipy for signal processing.

TODO: Implement advanced frequency analysis (FFT, wavelet transforms)
TODO: Add real-time analysis capabilities
TODO: Integrate with 528Hz healing frequency framework
TODO: Add support for multiple signal types (audio, biometric, etc.)
"""

import numpy as np
from scipy import signal, fft
from typing import List, Dict, Any, Tuple


# Solfeggio Frequencies - Reference for healing and resonance
SOLFEGGIO_FREQUENCIES = {
    174: "Pain Relief",
    285: "Energy & Safety",
    396: "Liberation from Fear",
    417: "Facilitation of Change",
    528: "Transformation & Miracles (DNA Repair)",
    639: "Connection & Relationships",
    741: "Awakening Intuition",
    852: "Spiritual Order",
    963: "Divine Consciousness"
}


def analyze_signal(signal_data: List[float], sample_rate: float = 1000.0) -> Dict[str, Any]:
    """
    Analyze vibrational signal to extract frequency information
    
    Args:
        signal_data: Time-series signal data
        sample_rate: Sampling rate in Hz (default: 1000 Hz)
        
    Returns:
        Dictionary containing:
        - dominant_frequencies: List of dominant frequencies
        - harmonic_patterns: Detected harmonic relationships
        - resonance_score: Overall resonance quality (0-1)
        - solfeggio_alignment: Alignment with Solfeggio frequencies
    
    TODO: This is a POC stub - implement full signal processing pipeline
    """
    # Convert to numpy array
    data = np.array(signal_data)
    
    # POC: Generate dummy frequency analysis
    # In production, use proper FFT and spectral analysis
    
    # Calculate FFT
    fft_values = np.fft.fft(data)
    fft_freq = np.fft.fftfreq(len(data), 1/sample_rate)
    
    # Get positive frequencies only
    positive_freq_idx = fft_freq > 0
    magnitudes = np.abs(fft_values[positive_freq_idx])
    frequencies = fft_freq[positive_freq_idx]
    
    # Find dominant frequencies (top 3)
    if len(magnitudes) > 0:
        top_indices = np.argsort(magnitudes)[-3:][::-1]
        dominant_frequencies = [float(frequencies[i]) for i in top_indices if i < len(frequencies)]
    else:
        # Fallback for POC
        dominant_frequencies = [528.0, 432.0, 396.0]
    
    # Calculate resonance score (0-1)
    # POC: Simple metric based on signal variance and mean
    resonance_score = float(np.clip(np.std(data) / (np.abs(np.mean(data)) + 1e-6), 0, 1))
    
    # Check alignment with Solfeggio frequencies
    solfeggio_alignment = _calculate_solfeggio_alignment(dominant_frequencies)
    
    # Detect harmonic patterns
    harmonic_patterns = _detect_harmonics(dominant_frequencies)
    
    return {
        "dominant_frequencies": dominant_frequencies,
        "harmonic_patterns": harmonic_patterns,
        "resonance_score": resonance_score,
        "solfeggio_alignment": solfeggio_alignment,
        "signal_quality": _assess_signal_quality(data)
    }


def _calculate_solfeggio_alignment(frequencies: List[float], tolerance: float = 10.0) -> Dict[str, Any]:
    """
    Calculate alignment with Solfeggio healing frequencies
    
    Args:
        frequencies: List of detected frequencies
        tolerance: Tolerance in Hz for matching (default: 10 Hz)
        
    Returns:
        Dictionary with alignment information
    """
    alignments = []
    
    for freq in frequencies:
        for solfeggio_freq, meaning in SOLFEGGIO_FREQUENCIES.items():
            if abs(freq - solfeggio_freq) <= tolerance:
                alignments.append({
                    "detected_frequency": freq,
                    "solfeggio_frequency": solfeggio_freq,
                    "meaning": meaning,
                    "deviation": abs(freq - solfeggio_freq)
                })
    
    return {
        "aligned_frequencies": alignments,
        "alignment_count": len(alignments),
        "primary_resonance": alignments[0]["meaning"] if alignments else None
    }


def _detect_harmonics(frequencies: List[float], tolerance: float = 0.02) -> Dict[str, Any]:
    """
    Detect harmonic relationships between frequencies
    
    Args:
        frequencies: List of frequencies to analyze
        tolerance: Relative tolerance for harmonic matching
        
    Returns:
        Dictionary describing harmonic patterns
    """
    harmonics = []
    
    # Check for integer ratios (harmonics)
    for i, f1 in enumerate(frequencies):
        for j, f2 in enumerate(frequencies[i+1:], start=i+1):
            if f1 == 0 or f2 == 0:
                continue
                
            ratio = f2 / f1 if f2 > f1 else f1 / f2
            
            # Check if ratio is close to an integer (harmonic relationship)
            nearest_integer = round(ratio)
            if abs(ratio - nearest_integer) < tolerance:
                harmonics.append({
                    "fundamental": min(f1, f2),
                    "harmonic": max(f1, f2),
                    "ratio": nearest_integer,
                    "type": _harmonic_type(nearest_integer)
                })
    
    return {
        "detected_harmonics": harmonics,
        "harmonic_count": len(harmonics),
        "harmonic_richness": len(harmonics) / max(len(frequencies), 1)
    }


def _harmonic_type(ratio: int) -> str:
    """Classify harmonic relationship"""
    harmonic_names = {
        1: "Unison",
        2: "Octave",
        3: "Perfect Fifth (12th)",
        4: "Double Octave",
        5: "Major Third (17th)",
        6: "Perfect Fifth + Octave"
    }
    return harmonic_names.get(ratio, f"Harmonic {ratio}")


def _assess_signal_quality(data: np.ndarray) -> Dict[str, Any]:
    """
    Assess overall signal quality
    
    Returns metrics like SNR, clarity, stability
    """
    return {
        "mean_amplitude": float(np.mean(np.abs(data))),
        "std_amplitude": float(np.std(data)),
        "dynamic_range": float(np.max(data) - np.min(data)),
        "zero_crossings": int(np.sum(np.diff(np.sign(data)) != 0)),
        "quality_score": float(np.clip(1.0 - np.std(data) / (np.max(np.abs(data)) + 1e-6), 0, 1))
    }


def generate_recommendations(analysis_results: Dict[str, Any]) -> List[str]:
    """
    Generate recommendations based on vibrational analysis
    
    Args:
        analysis_results: Results from analyze_signal()
        
    Returns:
        List of actionable recommendations
    """
    recommendations = []
    
    # Check resonance score
    if analysis_results["resonance_score"] < 0.3:
        recommendations.append("Consider practices to increase vibrational resonance (meditation, breathwork)")
    
    # Check Solfeggio alignment
    if analysis_results["solfeggio_alignment"]["alignment_count"] == 0:
        recommendations.append("Explore Solfeggio frequency music to enhance harmonic alignment")
    else:
        primary = analysis_results["solfeggio_alignment"]["primary_resonance"]
        recommendations.append(f"Your primary resonance aligns with: {primary}")
    
    # Check harmonic patterns
    if analysis_results["harmonic_patterns"]["harmonic_count"] == 0:
        recommendations.append("Work on developing harmonic balance through sound healing")
    
    # Signal quality
    if analysis_results["signal_quality"]["quality_score"] < 0.5:
        recommendations.append("Signal quality could be improved - ensure calm environment for analysis")
    
    return recommendations
