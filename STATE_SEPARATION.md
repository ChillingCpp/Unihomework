# STATE — Tách giọng hát khỏi giọng cãi nhau (3:07–3:20) — dừng chờ chuyển GPU

Ngày dừng: 2026-10-15 ~23:55. Tiến trình Demucs trên bản gốc đã KILL ở ~11% (PID 11188).
Thư mục `C:\Users\Admin\AppData\Local\Temp\opencode\demucs_orig\` chứa output DỞ — XÓA và chạy lại sau khi có GPU.

## File trong C:\Users\Admin\Desktop\baitap
- File remix (gốc, dual-mono, 4:11.59, 320kbps): tên bắt đầu "Đến Sau Một Người x Kết Thúc Lâu Rồi - (VietZ x Wi Remix)…"
- Bản gốc ca sĩ (12.2MB): tên bắt đầu "Đến Sau Một Người … Châu Khải Phong … Official Lyric Video…"
- Output suppression cũ (giữ làm baseline, KHÔNG phải separation):
  `... (CLEAN 3-07-3-20).mp3` (v1), `... (CLEAN v2 3-07-3-20).mp3` (v2), `... (CLEAN v3 3-07-3-20).mp3` (v3)
- `So sanh v* 187-200s (L-goc_R-da xu ly).wav` — file AB kiểm nghe

## Kết luận đã chốt (có bằng chứng)
1. Ca sĩ đoạn 187–200s = Châu Khải Phong (user xác nhận; ECAPA: hát sạch remix vs bản gốc 0.41, cửa sổ cãi nhau vs bản gốc 0.009 = embedding bị giọng nữ lấn át).
2. Demucs htdemucs: chỉ tách NHẠC (nhãn vocals gộp mọi giọng người) — stems 182–207s còn trong temp (`demucs_out/htdemucs/chunk_182_207/{vocals,no_vocals}.wav`).
3. Căn chỉnh theo bản gốc: THẤT BẠI sau 4 phép thử (chroma ≤0.18, f0 không khớp) → vocal remix biến đổi sâu; nhánh informed-subtraction DỪNG.
4. SepFormer-wsj02mix: SUY SỤP (out gần như mix đảo pha, corr ±0.95–0.98) → model tách mù tiếng Anh đọc KHÔNG phù hợp. DỪNG.
5. v1/v2/v3 = vocal SUPPRESSION (nén năng lượng), không phải separation. Không báo SDR.

## UniSE (QuarkAudio-UniSE, generative AR-LM) — THẤT BẠI cả 3 mode (có bằng chứng, file AB đã xóa khi dọn)
6. Setup: torch CUDA + RTX 4050; checkpoint `epoch=20-step=109367.ckpt` + BiCodec + xlsr-53; transformers pin 4.48.3; ckpt Linux→Windows convert; test_kwargs phải nằm dưới dataset_config.
7. mode tse (enroll = vocals gốc 70–80s): số đẹp (R argue 26%→7%, 0.8–1.5k -12dB, corr≈0) nhưng faithfulness trượt: chroma out–mix 0.176, f0 corr ÂM -0.72, ECAPA out–gốc 0.16–0.30 (chuẩn cùng-ca-sĩ 0.90) → model ẢO GIÁC nội dung. LOẠI.
8. mode ss (s1/s2) và se: chroma <0.5, corr≈0, ECAPA ≤0.05, arguefrac còn TỆ hơn mix (ss_s1 47.8%, se 57% vs mix 26%). LOẠI cả 3 mode generative.
9. Còn lại: (3) huấn luyện TSE phân biệt SpeakerBeam trên hỗn hợp tổng hợp từ bản gốc (tốn ngày+GPU, chưa chắc) hoặc (4) chốt v3 suppression. User đang cân nhắc thêm option (5): XÓA đoạn 187–200s và dựng lại bằng chất liệu trong file (transplant cùng câu / đắp đoạn khác / instrumental fill) — đang chờ quyết định mức can thiệp lời hát.

## Việc tiếp theo (sau khi có GPU NVIDIA)
1. `nvidia-smi` + cài torch CUDA (hiện torch 2.14 CPU-only; Python 3.14).
2. Chạy lại Demucs vocals bản gốc (dùng file temp ASCII `orig_ckp.mp3` để tránh lỗi unicode console) → enrollment dài.
3. Thử TSE **QuarkAudio-UniSE** (repo đã clone: temp `unified-audio/QuarkAudio-UniSE`; checkpoint trên HF; `mode: tse`, enroll 5s, 16kHz). CẢNH BÁO: model sinh (AR-LM+codec) có thể đổi lời hát — phải kiểm bằng tai; giọng hát+nhạc nền ngoài phân phối train.
4. Đánh giá 2 tầng: (T1) hỗn hợp tổng hợp từ giọng sạch ca sĩ + giọng nói khác → đo SI-SDRi thật; (T2) đoạn thật bằng nghe mù + soi spectrogram burst cãi nhau (187.0, 194–195, 198–199) + PYIN. Không ground truth → cấm tuyên bố SDR đoạn thật.
5. Fallback nếu UniSE tắc: giữ v3 suppression làm trần + báo trung thực.

## Script còn trong temp opencode
sepformer_trial.py, tempo_align_probe.py, f0_match.py, chroma_vmatch.py, chroma_cleanmatch.py, process_vocals*.py, chunk/final wav các bản.
