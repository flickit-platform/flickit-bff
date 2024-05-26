import Box from "@mui/material/Box";
import { Trans } from "react-i18next";
import {
  AssessmentKitInfoType,
  ExpertGroupDetails,
  ISubjectInfo,
  PathInfo,
} from "@types";
import Typography from "@mui/material/Typography";
import { getMaturityLevelColors, styles } from "@styles";
import { Link } from "react-router-dom";
import formatDate from "@/utils/formatDate";
import ColorfullProgress from "../common/progress/ColorfulProgress";
import { convertToRelativeTime } from "@/utils/convertToRelativeTime";
import { Button, Divider } from "@mui/material";
interface IAssessmentProgress {
  questionCount: number;
  answerCount: number;
}

export const AssessmentProgress = (props: IAssessmentProgress) => {
  const { questionCount, answerCount } = props;
  return (
    <Box
      display="flex"
      flexDirection="column"
      alignItems="center"
      justifyContent="center"
      textAlign="center"
      maxHeight="100%"
      gap={3}
      py={4}
      sx={{
        background: "#fff",
        boxShadow: "0px 0px 8px 0px rgba(0, 0, 0, 0.25)",
        borderRadius: "40px",
        px: { xs: 2, sm: 3 },
      }}
    >
      <ColorfullProgress
        questionCount={questionCount}
        answerCount={answerCount}
      />
    </Box>
  );
};
