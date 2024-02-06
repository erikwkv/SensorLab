# Bli kjent med databladet for AD-konverteren vi bruker.
## (a) Hvor mange klokkesykluser er det minste vi må bruke for å ta én punktprøve og overføre
dataene fra den tilbake til RPi?

Lest av fra databladet: 12 cycles for å convertere fra analog til digital + 1.5 cycles for "analog input sample time". + 2 på chip select og 0 bit. Til sammen og rundet opp blir dette 16 cycles.

## (b) Gitt en driftspenning på 3.3 V (V_dd), hva blir AD-konverterens oppløsning? Oppgi svaret i mV.

MCP3201 sin oppløsning er 12-bit = 2^12. Med V_ss som jord og V_dd = 3.3 V blir oppløsningen 3.3 V / 2^12 = 0.81 mV.

## (c) Gitt en driftspenning på 3.3 V (V_dd) og jord på V_ss, hvor mye større spenning enn V_dd, evt mindre enn V_ss, kan en pinne på AD-konverteren tåle?

Fra databladet til MCP3201 har vi at max verdi for V_dd = 7.0 V. Alle innganger og utganger tåler -0.6 V til V_dd + 0.6 V med V_ss som referansepunkt.

# 3. I dette laboppsettet benytter vi oss av såkalt Direct Memory Access (DMA). Hva er den store fordelen med dette (evt. hvilket problem relatert til sampling av data med Linux løser dette for oss)?

OS bruker en scheduler for å velge jobber fra listen av jobber å utføre. Dette gjør at OS ikke har tid til å ta imot og prosessere en kontinuerlig strøm av I/O fra enheter. Derfor kan vi bruke en DMA controller som en mellommann for å ta seg av I/O strømmen.