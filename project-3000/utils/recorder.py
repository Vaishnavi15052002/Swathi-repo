import traceback
from utils.logger import get_logger, PASS_LOG, FAIL_LOG

pass_logger = get_logger("PASS", PASS_LOG)
fail_logger = get_logger("FAIL", FAIL_LOG)


class TestRecorder:
    def __init__(self, tc_id, name, module, file):
        self.tc_id = tc_id
        self.name = name
        self.module = module
        self.file = file
        self.steps = []

    def step(self, text):
        self.steps.append(text)

    def log_pass(self):
        msg = (
            f"TestCaseName: {self.name} | "
            f"TestCaseID: {self.tc_id} | "
            f"Module: {self.module} | "
            f"Status: PASSED | "
            f"FilePath: {self.file}"
        )
        pass_logger.info(msg)

    def log_fail(self, exc):
        stacktrace = "".join(
            traceback.format_exception(type(exc), exc, exc.__traceback__)
        )

        msg = (
            f"TestCaseName: {self.name}\n"
            f"TestCaseID: {self.tc_id}\n"
            f"Module: {self.module}\n"
            f"Status: FAILED\n"
            f"ExceptionType: {type(exc).__name__}\n"
            f"FilePath: {self.file}\n"
            f"Steps:\n" +
            "\n".join(f"  - {s}" for s in self.steps) + "\n"
            f"StackTrace:\n{stacktrace}"
        )
        fail_logger.error(msg)
