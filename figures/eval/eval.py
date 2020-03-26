from matplotlib import pyplot as plt
import numpy as np
import json

"""
RECALL 2D/3D
"""
eval_virtual = json.load(open("./EvaluationVirtual/Evaluation/eval.json"))

labels = list(eval_virtual.keys())
recall_2d = [eval_virtual[k]["Segmentation2DEvaluation"]["recall"] for k in labels]
recall_3d = [eval_virtual[k]["PointCloudSegmentationEvaluation"]["recall"] for k in labels]

fig, ax = plt.subplots()
width = 0.35
x = np.arange(len(labels))
rects1 = ax.bar(x - width/2, recall_2d, width, label='2D Segmentation')
rects2 = ax.bar(x + width/2, recall_3d, width, label='3D Segmentation')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Recall')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()
plt.savefig("eval_recall.pdf")
plt.show()

"""
PRECISION 2D/3D
"""

precision_2d = [eval_virtual[k]["Segmentation2DEvaluation"]["precision"] for k in labels]
precision_3d = [eval_virtual[k]["PointCloudSegmentationEvaluation"]["precision"] for k in labels]

fig, ax = plt.subplots()
ax.set_ylim(0,1)
width = 0.35
x = np.arange(len(labels))
rects1 = ax.bar(x - width/2, precision_2d, width, label='2D Segmentation')
rects2 = ax.bar(x + width/2, precision_3d, width, label='3D Segmentation')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Precision')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()
plt.savefig("eval_precision.pdf")
plt.show()

"""
RECALL REAL VS VIRTUAL
"""

eval_real = json.load(open("./EvaluationReal/Evaluation/eval.json"))
recall_2d_real = [eval_real[k]["Segmentation2DEvaluation"]["recall"] for k in labels]

fig, ax = plt.subplots()
ax.set_ylim(0,1)
width = 0.35
x = np.arange(len(labels))
rects1 = ax.bar(x - width/2, recall_2d, width, label='Virtual plants')
rects2 = ax.bar(x + width/2, recall_2d_real, width, label='Real plants')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Recall')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()
plt.savefig("eval_recall_real.pdf")
plt.show()

"""
PRECISION REAL VS VIRTUAL
"""

precision_2d_real = [eval_real[k]["Segmentation2DEvaluation"]["precision"] for k in labels]

fig, ax = plt.subplots()
ax.set_ylim(0,1)
width = 0.35
x = np.arange(len(labels))
rects1 = ax.bar(x - width/2, precision_2d, width, label='Virtual plants')
rects2 = ax.bar(x + width/2, precision_2d_real, width, label='Real plants')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Precision')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()
plt.savefig("eval_precision_real.pdf")
plt.show()
