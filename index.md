---
title: Sonify
layout: template
filename: index.md
---

# Transferring Bits with Sound

## The Basic Idea

Our project goal is to transmit messages from one device to another using sound waves in the audible frequency range. Below, you can see a diagram of our system, which includes user input, conversion to binary, waveform encoding, and waveform decoding back into the original message (hopefully).

![](images/systemDiagram.png?raw=true)

## A Demo

Here is a demonstration of our software allowing a message to be transmitted from one device to another. The device on the right is encoding the message into the audible frequency and playing it through speakers, while the device on the left records the audio and analyzes it in the frequency domain to decode the message.

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YD8VOvXGZOg/0.jpg)](http://www.youtube.com/watch?v=YD8VOvXGZOg)

## Encoding Data

In order to store data in a sound wave, we decided to create a simple two-tone wave where a first tone, 1500 Hz, represents a binary 0 and a second tone, 2000 Hz, represents a binary 1. This generated two-tone wave is then transmitted over the first device's speakers.

![](images/encode.png?raw=true)

## Decoding Data

The decoding process begins with the second device streaming in audio and running a live fast fourier transform on the wave. This FFT allows us to analyze the wave in the frequency domain and see what frequency tones are most prevalent (typically either 1500 Hz or 2000 Hz).

![](images/decode.png?raw=true)

We use the information that we gather from the FFT to determine where there are sharp changes in frequency either from 1500 Hz to 2000 Hz or from 2000 Hz to 1500 Hz. When one of these two frquency change events occurs, we mark the current time and append it to an array.

![](images/decode1.png?raw=true)

When can then use this array of saved times to calculate how long each series of 0s and 1s occurred for and decode the original binary sequence, which allows us to get back the original tramsitted message.

![](images/decode2.png?raw=true)

## Accuracy Tradeoff

We made some tradeoffs and things.

![](images/tradeoff.png?raw=true)

## Future Work

Matched filters probably.
