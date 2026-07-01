from src.metrics import show_confusion_matrix_example, imbalanced_data_experiment
from src.dashboard import build_dashboard_html
from src.security import security_boundary_analysis
from src.answers import assessment_answers


def main():
    show_confusion_matrix_example()
    imbalanced_data_experiment()
    build_dashboard_html()
    security_boundary_analysis()
    assessment_answers()

main()
