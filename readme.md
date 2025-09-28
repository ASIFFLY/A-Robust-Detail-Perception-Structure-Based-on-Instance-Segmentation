## A Robust Detail Perception Structure Based on Instance Segmentation for Weld Seam Profile Extraction: Generalizability Perspective

## Motivation
Weld seam profile (WSP) extraction is critical for intelligent robotic welding with laser vision sensing. Current methods exhibit limitations in anti-interference capability, robustness, generalization capability, and precision when processing diverse joint types and complex backgrounds. This study introduces a novel YOLOv8-based WSP extraction structure to handle various joint types with enhanced robustness and generalization performance. The key innovations include: 1) a Cross-Stage Partial Fusion Block employing switchable multi-dilation convolutions to enhance multi-scale feature extraction for improved anti-interference ability; 2) an improved C2 module incorporating Multi-Scale Dilated Attention to boost the small-target detection and local detail perception; and 3) an Enhanced Channel-Spatial Attention module that dynamically enhances stripe-related features, thereby enhancing the model’s localization accuracy for WSP. Ablation studies confirm the effectiveness of each module, with the complete model achieving significant gains over the baseline: 3.20% (Precision), 1.25% (Recall), 2.88% (mAP@50), and 2.20% (F1-score). Comparative tests against six state-of-the-art models further highlight its robustness and superior generalization capability for WSP extraction.

## Data Preparation
[Download](https://pan.baidu.com/s/1Y8LbvXDJ-RErcEAm6aQCmg?pwd=b9dj download code: b9dj)

## Note
Due to pending patent applications, the source code and design documents pertaining to this work will be made publicly available upon patent grant.