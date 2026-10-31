-- Last updated: 31/10/2026, 19:01:24
# Write your MySQL query statement below
select sample_id, dna_sequence, species, CASE WHEN dna_sequence like 'ATG%' THEN 1 ELSE 0 END as 'has_start', CASE WHEN dna_sequence like '%TAA' or dna_sequence like '%TAG' or dna_sequence like '%TGA' THEN 1 ELSE 0 END as 'has_stop', CASE WHEN dna_sequence like '%ATAT%' THEN 1 ELSE 0 END as 'has_atat', CASE WHEN dna_sequence like '%GGG%' THEN 1 ELSE 0 END as 'has_ggg'
from Samples
order by 1