# Bli kjent med databladet for AD-konverteren vi bruker.
(a) Hvor mange klokkesykluser er det minste vi må bruke for å ta én punktprøve og overføre
dataene fra den tilbake til RPi?
(b) Gitt en driftspenning på 3.3 V (V_dd), hva blir AD-konverterens oppløsning? Oppgi
svaret i mV.
(c) Gitt en driftspenning på 3.3 V (V_dd) og jord på V_ss, hvor mye større spenning enn
V_dd, evt mindre enn V_ss, kan en pinne på AD-konverteren tåle?
4
3. I dette laboppsettet benytter vi oss av såkalt Direct Memory Access (DMA). Hva er den store
fordelen med dette (evt. hvilket problem relatert til sampling av data med Linux løser dette
for oss)?

# a) Lest av fra databladet: 12 cycles for å convertere fra analog til digital + 1.5 cycles for "analog input sample time". Til sammen og rundet opp blir dette 14 cycles.

# b) MCP3201 sin oppløsning er 12-bit = 2^12. Med V_ss som jord og V_dd = 3.3 V blir oppløsningen 3.3 V / 2^12 = 0.81 mV.

# c) Fra databladet til MCP3201 har vi at max verdi for V_dd = 7.0 V. Alle innganger og utganger tåler -0.6 V til V_dd + 0.6 V med V_ss som referansepunkt.