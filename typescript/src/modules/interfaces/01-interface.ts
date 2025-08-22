export const bootstrap = (): void => {
    interface Resume {
        fullName: string;
        email: string;
        skills: Skill[];
        addSkill?: (skill: Skill) => boolean // O ? indica que é opcional
    }

    interface Skill {
        name: string;
        level: 'beginner' | 'intermediate' | 'advanced'
    }

    // classe MyResume que tem a estrutura definida na interface Resume
    const MyResume: Resume = {
        fullName: 'Leticia',
        email: 'leticia@gmail.com',
        skills: [
            {name: 'javascript', level: 'advanced'},
            {name: 'TypeScript', level: 'beginner'},
        ]
    }

    console.log(MyResume);
};