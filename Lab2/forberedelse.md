# Forberedelsesoppgave 1

## Beskriv med Python-kode hvordan krysskorrelasjon kan brukes for å finne effektiv forsinkelse mellom to lydsignaler som har samplingsfrekvensen fs. Hint: du skal finne for hvilken forsinkelse som numpy.abs(krysskorrelasjonsfunksjonen) har maksimum.
```python
import numpy as np

def find_delay(signal1, signal2, fs):
    # Compute the cross-correlation between the two signals
    cross_correlation = np.correlate(signal1, signal2, mode='full')
    
    # Compute the time delays corresponding to each correlation value
    delays = np.arange(-len(signal2) + 1, len(signal1))
    time_delays = delays / fs
    
    # Find the index of the maximum correlation value
    max_index = np.argmax(np.abs(cross_correlation))
    
    # Compute the effective delay in seconds
    effective_delay = time_delays[max_index]
    
    return effective_delay

### Example usage
signal1 = np.array([1, 2, 3, 4, 5])
signal2 = np.array([0, 0, 1, 2, 3])
fs = 1  # Sampling frequency

delay = find_delay(signal1, signal2, fs)
print("Effective delay:", delay, "seconds")
```

# Forberedelsesoppgave 2

## Hvis du har et triangelformet array som i figur II.4, med sidelengde d, og samplingfrekvensen er fs; hva er maksimalt antall sampler med forsinkelse som kan oppstå?

Lydfart v = 343m/s
Pytagoras gir lengst avstand d lik:
d = np.sqrt(2)d

t = d/v [s]
antall sampler s = np.floor(t * f_s)

## Hvis du har et array med kun to mikrofoner, kan du detektere flere unike innfallsvinkler om maksimal forsinkelse mellom dem er 2 sampel eller 4 sampel? Hint: Et lite vinkelområde vil gi samme forsinkelse, n21, grunnet avrunding til helt antall sampel!
Jo flere sampler jo flere verdier kan man runde til
-> flere sampler med forsinkelse fører til flere sektorer med avrundingsvinkler