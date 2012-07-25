# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# NOTE: this file is autogenerated by ffmpeg/chromium/scripts/generate_gyp.py

{
  'conditions': [
    ['((target_arch == "arm" and arm_neon == 1)) and (ffmpeg_branding == "Chrome" or ffmpeg_branding == "ChromeOS")', {
      'sources': [
        'libavcodec/arm/aacpsdsp_neon.S',
        'libavcodec/arm/h264cmc_neon.S',
        'libavcodec/arm/h264dsp_neon.S',
        'libavcodec/arm/h264idct_neon.S',
        'libavcodec/arm/sbrdsp_neon.S',
      ],
    }],  # ((target_arch == "arm" and arm_neon == 1)) and (ffmpeg_branding == "Chrome" or ffmpeg_branding == "ChromeOS")
    ['(target_arch == "ia32" or target_arch == "x64") and (ffmpeg_branding == "Chrome" or ffmpeg_branding == "ChromeOS")', {
      'sources': [
        'libavcodec/x86/dct32_sse.asm',
        'libavcodec/x86/h264_chromamc.asm',
        'libavcodec/x86/h264_chromamc_10bit.asm',
        'libavcodec/x86/h264_deblock.asm',
        'libavcodec/x86/h264_deblock_10bit.asm',
        'libavcodec/x86/h264_idct.asm',
        'libavcodec/x86/h264_idct_10bit.asm',
        'libavcodec/x86/h264_weight.asm',
        'libavcodec/x86/h264_weight_10bit.asm',
        'libavcodec/x86/h264dsp_mmx.c',
        'libavcodec/x86/imdct36_sse.asm',
        'libavcodec/x86/mpegaudiodec_mmx.c',
        'libavcodec/x86/sbrdsp.asm',
        'libavcodec/x86/sbrdsp_init.c',
      ],
    }],  # (target_arch == "ia32" or target_arch == "x64") and (ffmpeg_branding == "Chrome" or ffmpeg_branding == "ChromeOS")
    ['(1) and (ffmpeg_branding == "ChromeOS")', {
      'sources': [
        'libavcodec/acelp_filters.c',
        'libavcodec/acelp_pitch_delay.c',
        'libavcodec/acelp_vectors.c',
        'libavcodec/amrnbdec.c',
        'libavcodec/amrwbdec.c',
        'libavcodec/celp_filters.c',
        'libavcodec/celp_math.c',
        'libavcodec/flvdec.c',
        'libavcodec/gsm_parser.c',
        'libavcodec/gsmdec.c',
        'libavcodec/gsmdec_data.c',
        'libavcodec/h263.c',
        'libavcodec/h263_parser.c',
        'libavcodec/h263dec.c',
        'libavcodec/intelh263dec.c',
        'libavcodec/ituh263dec.c',
        'libavcodec/lsp.c',
        'libavcodec/mpeg4video.c',
        'libavcodec/mpeg4video_parser.c',
        'libavcodec/mpeg4videodec.c',
        'libavcodec/msgsmdec.c',
        'libavformat/amr.c',
        'libavformat/avidec.c',
        'libavformat/gsmdec.c',
      ],
    }],  # (1) and (ffmpeg_branding == "ChromeOS")
    ['(target_arch == "arm" or (target_arch == "arm" and arm_neon == 1)) and (ffmpeg_branding == "Chrome" or ffmpeg_branding == "ChromeOS")', {
      'sources': [
        'libavcodec/arm/aacpsdsp_init_arm.c',
        'libavcodec/arm/h264dsp_init_arm.c',
        'libavcodec/arm/mpegaudiodsp_fixed_armv6.S',
        'libavcodec/arm/mpegaudiodsp_init_arm.c',
        'libavcodec/arm/sbrdsp_init_arm.c',
      ],
    }],  # (target_arch == "arm" or (target_arch == "arm" and arm_neon == 1)) and (ffmpeg_branding == "Chrome" or ffmpeg_branding == "ChromeOS")
    ['((target_arch == "arm" and arm_neon == 1)) and (1)', {
      'sources': [
        'libavcodec/arm/dsputil_init_neon.c',
        'libavcodec/arm/dsputil_neon.S',
        'libavcodec/arm/fft_fixed_neon.S',
        'libavcodec/arm/fft_neon.S',
        'libavcodec/arm/fmtconvert_neon.S',
        'libavcodec/arm/h264pred_neon.S',
        'libavcodec/arm/int_neon.S',
        'libavcodec/arm/mdct_fixed_neon.S',
        'libavcodec/arm/mdct_neon.S',
        'libavcodec/arm/mpegvideo_neon.S',
        'libavcodec/arm/rdft_neon.S',
        'libavcodec/arm/simple_idct_neon.S',
        'libavcodec/arm/vp3dsp_neon.S',
        'libavcodec/arm/vp8dsp_init_neon.c',
        'libavcodec/arm/vp8dsp_neon.S',
        'libavutil/arm/float_dsp_init_neon.c',
        'libavutil/arm/float_dsp_neon.S',
      ],
    }],  # ((target_arch == "arm" and arm_neon == 1)) and (1)
    ['(target_arch == "ia32" or target_arch == "x64") and (1)', {
      'sources': [
        'libavcodec/x86/deinterlace.asm',
        'libavcodec/x86/dsputil_mmx.c',
        'libavcodec/x86/dsputil_yasm.asm',
        'libavcodec/x86/fdct_mmx.c',
        'libavcodec/x86/fft.c',
        'libavcodec/x86/fft_3dn.c',
        'libavcodec/x86/fft_3dn2.c',
        'libavcodec/x86/fft_mmx.asm',
        'libavcodec/x86/fmtconvert.asm',
        'libavcodec/x86/fmtconvert_mmx.c',
        'libavcodec/x86/h264_intrapred.asm',
        'libavcodec/x86/h264_intrapred_10bit.asm',
        'libavcodec/x86/h264_intrapred_init.c',
        'libavcodec/x86/h264_qpel_10bit.asm',
        'libavcodec/x86/idct_mmx_xvid.c',
        'libavcodec/x86/idct_sse2_xvid.c',
        'libavcodec/x86/motion_est_mmx.c',
        'libavcodec/x86/mpegvideo_mmx.c',
        'libavcodec/x86/simple_idct_mmx.c',
        'libavcodec/x86/vp3dsp.asm',
        'libavcodec/x86/vp3dsp_init.c',
        'libavcodec/x86/vp8dsp-init.c',
        'libavcodec/x86/vp8dsp.asm',
        'libavutil/x86/cpu.c',
        'libavutil/x86/float_dsp.asm',
        'libavutil/x86/float_dsp_init.c',
      ],
    }],  # (target_arch == "ia32" or target_arch == "x64") and (1)
    ['(1) and (ffmpeg_branding == "Chrome" or ffmpeg_branding == "ChromeOS")', {
      'sources': [
        'libavcodec/aac_ac3_parser.c',
        'libavcodec/aac_parser.c',
        'libavcodec/aacadtsdec.c',
        'libavcodec/aacdec.c',
        'libavcodec/aacps.c',
        'libavcodec/aacpsdsp.c',
        'libavcodec/aacsbr.c',
        'libavcodec/aactab.c',
        'libavcodec/ac3tab.c',
        'libavcodec/cabac.c',
        'libavcodec/dct.c',
        'libavcodec/dct32_fixed.c',
        'libavcodec/dct32_float.c',
        'libavcodec/error_resilience.c',
        'libavcodec/h264.c',
        'libavcodec/h264_cabac.c',
        'libavcodec/h264_cavlc.c',
        'libavcodec/h264_direct.c',
        'libavcodec/h264_loopfilter.c',
        'libavcodec/h264_parser.c',
        'libavcodec/h264_ps.c',
        'libavcodec/h264_refs.c',
        'libavcodec/h264_sei.c',
        'libavcodec/h264dsp.c',
        'libavcodec/h264idct.c',
        'libavcodec/kbdwin.c',
        'libavcodec/mpegaudio.c',
        'libavcodec/mpegaudio_parser.c',
        'libavcodec/mpegaudiodec.c',
        'libavcodec/mpegaudiodecheader.c',
        'libavcodec/mpegaudiodsp.c',
        'libavcodec/mpegaudiodsp_fixed.c',
        'libavcodec/mpegaudiodsp_float.c',
        'libavcodec/mpegvideo.c',
        'libavcodec/sbrdsp.c',
        'libavcodec/sinewin.c',
        'libavcodec/timecode.c',
        'libavformat/mov.c',
        'libavformat/mov_chan.c',
        'libavformat/mp3dec.c',
      ],
    }],  # (1) and (ffmpeg_branding == "Chrome" or ffmpeg_branding == "ChromeOS")
    ['(1) and (ffmpeg_branding == "ChromiumOS" or ffmpeg_branding == "ChromeOS")', {
      'sources': [
        'libavcodec/flac_parser.c',
        'libavcodec/flacdec.c',
        'libavcodec/flacdsp.c',
        'libavformat/flacdec.c',
        'libavformat/rawdec.c',
      ],
    }],  # (1) and (ffmpeg_branding == "ChromiumOS" or ffmpeg_branding == "ChromeOS")
    ['(target_arch == "arm" or (target_arch == "arm" and arm_neon == 1)) and (1)', {
      'sources': [
        'libavcodec/arm/dsputil_arm.S',
        'libavcodec/arm/dsputil_armv6.S',
        'libavcodec/arm/dsputil_init_arm.c',
        'libavcodec/arm/dsputil_init_armv5te.c',
        'libavcodec/arm/dsputil_init_armv6.c',
        'libavcodec/arm/dsputil_init_vfp.c',
        'libavcodec/arm/dsputil_vfp.S',
        'libavcodec/arm/fft_fixed_init_arm.c',
        'libavcodec/arm/fft_init_arm.c',
        'libavcodec/arm/fmtconvert_init_arm.c',
        'libavcodec/arm/fmtconvert_vfp.S',
        'libavcodec/arm/h264pred_init_arm.c',
        'libavcodec/arm/jrevdct_arm.S',
        'libavcodec/arm/mpegvideo_arm.c',
        'libavcodec/arm/mpegvideo_armv5te.c',
        'libavcodec/arm/mpegvideo_armv5te_s.S',
        'libavcodec/arm/simple_idct_arm.S',
        'libavcodec/arm/simple_idct_armv5te.S',
        'libavcodec/arm/simple_idct_armv6.S',
        'libavcodec/arm/vp3dsp_init_arm.c',
        'libavcodec/arm/vp8_armv6.S',
        'libavcodec/arm/vp8dsp_armv6.S',
        'libavcodec/arm/vp8dsp_init_arm.c',
        'libavcodec/arm/vp8dsp_init_armv6.c',
        'libavutil/arm/cpu.c',
        'libavutil/arm/float_dsp_init_arm.c',
        'libavutil/arm/float_dsp_init_vfp.c',
        'libavutil/arm/float_dsp_vfp.S',
      ],
    }],  # (target_arch == "arm" or (target_arch == "arm" and arm_neon == 1)) and (1)
    ['(1) and (1)', {
      'sources': [
        'libavcodec/allcodecs.c',
        'libavcodec/audioconvert.c',
        'libavcodec/avfft.c',
        'libavcodec/avpacket.c',
        'libavcodec/bitstream.c',
        'libavcodec/bitstream_filter.c',
        'libavcodec/dirac.c',
        'libavcodec/dsputil.c',
        'libavcodec/faanidct.c',
        'libavcodec/fft_fixed.c',
        'libavcodec/fft_float.c',
        'libavcodec/flac.c',
        'libavcodec/flacdata.c',
        'libavcodec/fmtconvert.c',
        'libavcodec/frame_thread_encoder.c',
        'libavcodec/golomb.c',
        'libavcodec/h264pred.c',
        'libavcodec/imgconvert.c',
        'libavcodec/jrevdct.c',
        'libavcodec/mdct_fixed.c',
        'libavcodec/mdct_float.c',
        'libavcodec/mpeg12data.c',
        'libavcodec/mpeg4audio.c',
        'libavcodec/mpegaudiodata.c',
        'libavcodec/options.c',
        'libavcodec/parser.c',
        'libavcodec/pcm.c',
        'libavcodec/pthread.c',
        'libavcodec/raw.c',
        'libavcodec/rawdec.c',
        'libavcodec/rdft.c',
        'libavcodec/simple_idct.c',
        'libavcodec/utils.c',
        'libavcodec/vorbis.c',
        'libavcodec/vorbis_data.c',
        'libavcodec/vorbis_parser.c',
        'libavcodec/vorbisdec.c',
        'libavcodec/vp3.c',
        'libavcodec/vp3_parser.c',
        'libavcodec/vp3dsp.c',
        'libavcodec/vp56rac.c',
        'libavcodec/vp8.c',
        'libavcodec/vp8_parser.c',
        'libavcodec/vp8dsp.c',
        'libavcodec/xiph.c',
        'libavformat/allformats.c',
        'libavformat/avio.c',
        'libavformat/aviobuf.c',
        'libavformat/cutils.c',
        'libavformat/id3v1.c',
        'libavformat/id3v2.c',
        'libavformat/isom.c',
        'libavformat/matroska.c',
        'libavformat/matroskadec.c',
        'libavformat/metadata.c',
        'libavformat/oggdec.c',
        'libavformat/oggparsecelt.c',
        'libavformat/oggparsedirac.c',
        'libavformat/oggparseflac.c',
        'libavformat/oggparseogm.c',
        'libavformat/oggparseopus.c',
        'libavformat/oggparseskeleton.c',
        'libavformat/oggparsespeex.c',
        'libavformat/oggparsetheora.c',
        'libavformat/oggparsevorbis.c',
        'libavformat/options.c',
        'libavformat/pcm.c',
        'libavformat/riff.c',
        'libavformat/rm.c',
        'libavformat/rmdec.c',
        'libavformat/seek.c',
        'libavformat/subtitles.c',
        'libavformat/utils.c',
        'libavformat/vorbiscomment.c',
        'libavformat/wav.c',
        'libavutil/audio_fifo.c',
        'libavutil/audioconvert.c',
        'libavutil/avstring.c',
        'libavutil/base64.c',
        'libavutil/blowfish.c',
        'libavutil/bprint.c',
        'libavutil/cpu.c',
        'libavutil/crc.c',
        'libavutil/dict.c',
        'libavutil/eval.c',
        'libavutil/fifo.c',
        'libavutil/float_dsp.c',
        'libavutil/imgutils.c',
        'libavutil/intfloat_readwrite.c',
        'libavutil/inverse.c',
        'libavutil/lfg.c',
        'libavutil/log.c',
        'libavutil/lzo.c',
        'libavutil/mathematics.c',
        'libavutil/md5.c',
        'libavutil/mem.c',
        'libavutil/opt.c',
        'libavutil/parseutils.c',
        'libavutil/pixdesc.c',
        'libavutil/random_seed.c',
        'libavutil/rational.c',
        'libavutil/samplefmt.c',
        'libavutil/sha.c',
        'libavutil/time.c',
        'libavutil/timecode.c',
        'libavutil/utils.c',
        'libavutil/xtea.c',
      ],
    }],  # (1) and (1)
  ],  # conditions
}
