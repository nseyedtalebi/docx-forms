#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docxtpl import DocxTemplate
import sys

def make_variant_table_entry(gene=None,
                             transcript=None,
                             genome=None,
                             chrom=None,
                             start=None,
                             end=None,
                             ref=None,
                             variant=None):
    """
    Returns a dict for use in the template document variant table
    Different from make_variant_list_entry!
    """
    return {"gene": gene,
            "transcript": transcript,
            "genome": genome,
            "chrom": chrom,
            "start": start,
            "end": end,
            "ref": ref,
            "variant": variant
            }

def make_variant_list_entry(gene=None,
                            allele_frequency=None,
                            mutation=None,
                            interpretation="Enter interpretation here"
                            ):
    """
    Returns a dict for use in the variant section of the template.
    Different from make_variant_table_entry!
    """
    return {"gene": gene,
            "allele_frequency": allele_frequency,
            "mutation": mutation,
            "interpretation": interpretation
            }

doc = DocxTemplate(sys.argv[1])
context = { 'nvariants' : "999",
           'variant_list': [
               make_variant_list_entry(*args)
               for args in (('TEST1',101,'MUT1'),('TEST2',102,'MUT2'))
           ],
           'variant_tbl_entries':[
               make_variant_table_entry(*args)
               for args in (
                   ('TEST1','TRANSCRIPT1','Hg19','chr1','000000','999999','G','A'),
                   ('TEST2','TRANSCRIPT2','Hg19','chr2','000000','999999','C','G'),
               )
           ],
           }
doc.render(context)
doc.save("generated_doc.docx")
