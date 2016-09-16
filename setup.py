from setuptools.command.install import install
from distutils.core import setup, Extension

class Build_ext_first(install):
    def run(self):
        self.run_command("build_ext")
        return install.run(self)

xraylib_extension = Extension('_xraylib', 
                              sources=['src/xrayvars.c',
                                       'src/cross_sections.c',
                                       'src/scattering.c',
                                       'src/atomicweight.c',
			               'src/edges.c',
			               'src/fluor_lines.c',
                                       'src/fluor_yield.c',
				       'src/jump.c',
                                       'src/coskron.c',
                                       'src/radrate.c',
                                       'src/cs_line.c',         
                                       'src/polarized.c',
                                       'src/splint.c',
                                       'src/cs_barns.c',
                                       'src/fi.c',
                                       'src/fii.c',
                                       'src/kissel_pe.c',
                                       'src/xrayfiles_inline.c',
                                       'src/xraylib-aux.c',
                                       'src/xraylib-parser.c',
                                       'src/cs_cp.c',
                                       'src/refractive_indices.c',
                                       'src/comptonprofiles.c',
                                       'src/atomiclevelwidth.c',
                                       'src/auger_trans.c',
                                       'src/xrf_cross_sections_aux.c',
                                       'src/crystal_diffraction.c',
                                       'src/xraylib-nist-compounds.c',
                                       'src/densities.c',
                                       'src/xraylib-radionuclides.c',
                                       'src/xrayglob_inline.c',
                                       'xraylib.i',
                                      ],       
                              include_dirs=['src','include','.'],
                              swig_opts=['-includeall', '-I./include'],
                              libraries=['m'])


setup(name = 'xraylib',
      version = '3.1',
      author      = "Tom Schoonjans",
      py_modules = ["xraylib"],
      ext_modules=[xraylib_extension],
      cmdclass = {'install' : Build_ext_first},
     )
